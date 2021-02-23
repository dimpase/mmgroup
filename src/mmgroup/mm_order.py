import sys
import os

sys.path.append(r"C:\Data\projects\MonsterGit\src")

import numpy as np

from mmgroup import structures
from mmgroup.mat24 import vect_to_cocode
from mmgroup.mat24 import ploop_theta
from mmgroup.mm import mm_aux_index_sparse_to_leech2
from mmgroup.mm import mm_vector
from mmgroup.mm import mm_aux_mmv_extract_sparse_signs
from mmgroup.mm_group import MMGroup, MMGroupWord
from mmgroup.mm_space import MMSpace
from mmgroup.generators import mm_group_check_word_n
from mmgroup.generators import mm_group_words_equ
from mmgroup.generators import mm_group_n_mul_element
from mmgroup.generators import mm_group_n_reduce_word 
from mmgroup.generators import gen_leech3to2_type4
from mmgroup.generators import gen_leech2_reduce_type4
from mmgroup.clifford12 import leech3matrix_kernel_vector
from mmgroup.clifford12 import leech3matrix_watermark
from mmgroup.clifford12 import leech3matrix_watermark_perm_num
from mmgroup.clifford12 import leech2matrix_add_eqn
from mmgroup.clifford12 import leech2matrix_solve_eqn
from mmgroup.mm15 import op_copy as mm_op15_copy
from mmgroup.mm15 import op_compare as mm_op15_compare
from mmgroup.mm15 import op_word as mm_op15_word
from mmgroup.mm15 import op_word_tag_A as mm_op15_word_tag_A 
from mmgroup.mm15 import op_omega as mm_op15_omega 




MMV3 = MMSpace(3)
MMV15 = MMSpace(15)
MM = MMV3.group
assert  MMV15.group == MM


ORDER_VECTOR = None
DIAG_VA = TAGS_Y = TAGS_X = TAG_SIGN = None
WATERMARK_PERM = SOLVE_X = SOLVE_Y = None


def stabilizer_vector(v, g, n):
    """Compute a vector stabilized by an element of the monster

    Le ``g`` be an element of the monster group of order ``n`` and 
    ``v`` a vector in a represention of the monster. We return the
    vector ``sum(v * g**i for i  in range(n))`` which is stabilized
    by ``g``. We always return ``None`` if that sum is 0 or a 
    multiple of the 1 element in the representation space. The 
    last condition is checked with a fast crude check only.  
    """
    vg = v.copy()
    w = v.copy()
    for i in range(1, n):
        vg *= g 
        w += vg
    assert v == vg * g
    if (w['B'] == 0).all():
        return None
    return w


def make_order_vector(s_g71, s_v71, s_gA, diag, s_g94, s_v94):
    v71 = 10 * MMV15(s_v71)
    g71 = MM(s_g71)
    w71 = stabilizer_vector(v71, g71, 71)
    assert w71 is not None
    w71 *= MM(s_gA)
    v94 = 6 * MMV15(s_v94)
    g94 = MM(s_g94)
    w94 = stabilizer_vector(v94 - v94 * g94, g94**2, 47)
    assert w94 is not None
    w = w71 + w94
    v3 = leech3matrix_kernel_vector(15, w.data, diag)
    assert v3 != 0
    v_type4 = gen_leech3to2_type4(v3)
    assert v_type4 == 0x800000
    w.reduce()
    return w


def compute_order_vector(recompute = False, verbose = 0):
    global ORDER_VECTOR, DIAG_VA, TAGS_Y, TAGS_X, TAG_SIGN 
    global WATERMARK_PERM, SOLVE_Y, SOLVE_X

    try:
        assert not recompute
        from mmgroup.structures import order_vector_data
    except (ImportError, AssertionError):
        from mmgroup.structures import find_order_vector
        result = find_order_vector.find_order_vector(verbose)
        find_order_vector.write_order_vector(result)
        from mmgroup.structures import order_vector_data
        del find_order_vector
    from mmgroup.structures.order_vector_data import S_G71, S_V71
    from mmgroup.structures.order_vector_data import S_GA, DIAG_VA
    from mmgroup.structures.order_vector_data import S_G94, S_V94
    ORDER_VECTOR =  make_order_vector(
        S_G71, S_V71, S_GA, DIAG_VA, S_G94, S_V94
    )
    assert ORDER_VECTOR is not None
    OV = ORDER_VECTOR.data
    DIAG_VA = order_vector_data.DIAG_VA
    TAGS_Y = np.array(order_vector_data.TAGS_Y, dtype = np.uint32) 
    TAGS_X = np.array(order_vector_data.TAGS_X, dtype = np.uint32)
    TAG_SIGN =  np.array([order_vector_data.TAG_SIGN], dtype = np.uint32) 
    WATERMARK_PERM = np.zeros(24, dtype = np.uint32)
    ok = leech3matrix_watermark(15, OV, WATERMARK_PERM)
    assert ok >= 0

    SOLVE_Y = np.zeros(11, dtype = np.uint64)
    assert len(TAGS_Y) == 11
    nrows = 0
    for y in TAGS_Y:
        i, j = (y >> 14) & 0x1f, (y >> 8) & 0x1f
        vect = (1 << i) + (1 << j)
        eqn = vect_to_cocode(vect) & 0x7ff
        nrows += leech2matrix_add_eqn(SOLVE_Y, nrows, 11, eqn)
        #print(hex(y), hex(eqn), nrows)
    assert nrows == 11, nrows
    assert mm_aux_mmv_extract_sparse_signs(15, OV, TAGS_Y, 11) == 0
    
    SOLVE_X = np.zeros(24, dtype = np.uint64)
    assert len(TAGS_X) == 24
    nrows = 0
    for x in TAGS_X:
        eqn =  mm_aux_index_sparse_to_leech2(x)  
        nrows += leech2matrix_add_eqn(SOLVE_X, nrows, 24, eqn)
        #print(hex(x), hex(eqn), nrows)
    assert nrows == 24, nrows
    assert mm_aux_mmv_extract_sparse_signs(15, OV, TAGS_X, 24) == 0


def get_order_vector(recompute = False, verbose = 0):
    if not recompute and ORDER_VECTOR is not None:
        return ORDER_VECTOR
    compute_order_vector(recompute, verbose)
    return ORDER_VECTOR



###########################################################################
# Check equality of two elements of the monster
###########################################################################
 

def check_mm_equal(g1, g2, mode = 0):
    """Return ``g1 == g2`` for elements ``g1, g2`` of the monster.

    If ``mode == 0`` (default) we first try to check equality inside 
    in the subgroup ``N_0`` of the monster, which may be considerbly 
    faster. 

    If ``mode != 0`` or this is not possible we check if 
    ``v * g1 * g2**(-1) == v`` holds for the *ORDER_VECTOR* ``v``. 

    We just check the data in ``g1`` and ``g2``, ingnoring
    ``g1.group`` and ``g2.group``.
    """
    assert isinstance(g1, MMGroupWord)
    assert isinstance(g2, MMGroupWord)
    g3 = np.zeros(2 * (g1.length + g2.length) + 1, dtype = np.uint32)
    status = mm_group_words_equ(g1._data, g1.length,
        g2._data, g2.length, g3)
    if status < 2:
        return not status

    v = get_order_vector().data
    w = mm_vector(15)
    work = mm_vector(15)
    mm_op15_copy(v, w)
    mm_op15_word(w, g3, status - 2, 1, work)
    return not mm_op15_compare(v, w)



###########################################################################
# Computing the order of an element of the monster
###########################################################################


def check_mm_order(g, max_order = 119, mode = 0):
    """Return order of monster group element ``g``.

    if ``order(g) < max_order`` return ``order(g)``; else return ``0``.

    If mode is ``0`` (default) we first check if ``g`` is in the 
    subgroup ``N_0 of`` the monster. If this is the case the we check 
    the order of ``g``  by calculating in ``N_0``.

    Othewise we compute the minimum ``i`` such that
    ``v * g**i == v`` for the *order vector* ``v`. 
    """
    assert isinstance(g, MMGroupWord)
    g.reduce()
    if mode == 0:
        n0 = np.zeros(5, dtype = np.uint32)
        status = mm_group_check_word_n(g._data, g.length, n0)
        if status == 0:
            return 1
        if status == 1:
            n1 = np.copy(n0)
            for i in range(2, max_order+1):
                mm_group_n_mul_element(n1, n0)
                if not mm_group_n_reduce_word(n1):
                    return i
            return 0

    v = get_order_vector().data
    w = mm_vector(15)
    work = mm_vector(15)
    mm_op15_copy(v, w)
    for i in range(1, max_order+1):
        mm_op15_word(w, g._data, g.length, 1, work)
        if not mm_op15_compare(v, w):
            return i
    return 0



###########################################################################
# Check if an element of the monster is in the subgroup G_x0
###########################################################################
 
def check_mm_in_g_x0(g):
    """Check if ``g`` is in the subgroup ``G_x0`` of the monster
   
    If ``g`` is in the subgroup ``G_x0`` of the monster then the
    function changes the word representing ``g`` to a (uniquely 
    defined) word in the generators of the subgroup ``G_x0`` and
    returns ``g``.  
    
    Otherwise the function does not change ``g`` and returns ``None``.
    
    ``g`` must be an instance of class 
    ``mmgroup.mm_group.MMGroupWord``.
   
    Not yet tested!!!
    
    """
    assert isinstance(g, MMGroupWord)
    v = get_order_vector().data
    w = mm_vector(15)
    work = mm_vector(15)
    mm_op15_copy(v, w)
    mm_op15_word(w, g.data, len(g.data) - 2, 1, work)
    w3 = leech3matrix_kernel_vector(15, w.data, DIAG_VA)
    if w3 == 0: 
        return None
    w_type4 = gen_leech3to2_type4(w3)
    if w_type4 == 0: 
        return None
    wA = w.data[:2*24]
    g1i = np.zeros(11, dtype = np.uint32)
    len_g1 = gen_leech2_reduce_type4(w_type4, g1i)
    assert len_result >= 0 
    mm_op15_word_tag_A(wA, g1i, len_g1)
    perm_num = leech3matrix_watermark_perm_num(15, WATERMARK_PERM, wA)
    if perm_num < 0: 
        return None
    if perm_num > 0:
        g1i[len_g1] = 0xA0000000 + perm_num
        mm_op15_word_tag_A(wA, g1i[len_g1:], 1)
        len_g1 += 1
    v_y = mm_aux_mmv_extract_sparse_signs(15, wA, TAGS_Y, 11)
    if v_y < 0:
        return None
    y = leech2matrix_solve_eqn(SOLVE_Y, 11, v_y)
    if y > 0:
        g1i[len_g1] = 0xC0000000 + y
        mm_op15_word_tag_A(wA, g1i[len_g1:], 1)
        len_g1 += 1
    if wA != v[:2*24]:
        return None
    mm_op15_word(w, g1i, len(g1), 1, work)
    v_x = mm_aux_mmv_extract_sparse_signs(15, w, TAGS_X, 24)
    if v_x < 0:
        return None
    x = leech2matrix_solve_eqn(SOLVE_X, 24, v_x)
    d = ((x >> 12) ^ ploop_theta(x)) & 0xfff
    x &= 0xfff 
    len_g1_new  = 0  
    if x > 0:
        g1i[len_g1] = 0xB0000000 + x
        len_g1_new += 1
    if d > 0:
        g1i[len_g1] = 0x90000000 + d
        len_g1_new += 1
    mm_op15_word(w, g1i[len_gl:], len_g1_new)    
    len_g1 += len_g1_new
    sign = mm_aux_mmv_extract_sparse_signs(15, w, TAG_SIGN, 1)
    if sign < 0:
        return None
    if sign:
        mm_op15omega(w, sign << 12) 
        g1i[len_g1] = 0xB0001000 
        len_g1_new += 1
    if mm_op15_compare(v, w):
        return None
    g._extend(11)
    g.length = len_g1
    g.reduced = 0
    for i in range(len_g1):
        f._data[i] = w[len_1 - 1 - i] ^ 0x80000000
    return g.reduce()
    


###########################################################################
# Main program (for testing)
###########################################################################


if __name__ == "__main__":
   get_order_vector(recompute = 0, verbose = 1)





