r"""We deal with the representation of elements of the monster group. 

Generators of the monster group :math:`\mathbb{M}`
..................................................

Conway :cite:`Con85` has constructed a ``196884``-dimensional rational 
representation :math:`\rho` of the monster :math:`\mathbb{M}` based on 
representations of two subgroups 
:math:`G_{x0} = 2_+^{1+24}.\mbox{Co}_1` and 
:math:`N_0 = 2^{2+11+22}.( M_{24} \times S_3)` of 
:math:`\mathbb{M}` which generate :math:`\mathbb{M}`. 
Here :math:`G_{x0}` has a normal extraspecial ``2``-subgroup 
:math:`2_+^{1+24}` with factor group :math:`\mbox{Co}_1`, where
:math:`\mbox{Co}_1` is the automorphism group of the Leech lattice
modulo ``2``. The group :math:`N_0` has a normal subgroup
:math:`2^{2+11+22}`, which is a certain ``2`` group and the factor
group is a direct product of the Mathieu group :math:`M_{24}`
and the symmetric permutation group :math:`S_3` of ``3`` elements.

The group :math:`N_{x0} = N_0 \cap G_{x0}` has index ``3`` in
:math:`N_{0}` and structure :math:`2^{1+24} . 2^{11} . M_{24}`.
It is generated by elements  :math:`x_\delta`, :math:`x_\pi`, 
:math:`x_e`, :math:`y_e`, :math:`z_e`, for all
:math:`x_\delta \in \mathcal{C}^*`, 
:math:`\pi \in {{\rm Aut}_{{\rm St}} \mathcal{P}}` and 
:math:`e \in  \mathcal{P}`.

Here  :math:`\mathcal{C}^*` is the Golay cocode defined in
section  :ref:`golay-label`, :math:`\mathcal{P}` is the Parker
loop defined in section  :ref:`parker-loop-label`, and 
:math:`{{\rm Aut}_{{\rm St}} \mathcal{P}}` is the automorphism 
group of  :math:`\mathcal{P}` defined in section  
:ref:`aut_ploop_label`.
The group :math:`N_{0}` has a subgroup isomorphic to
:math:`{{\rm Aut}_{{\rm St}} \mathcal{P}}` generated by the
generators  :math:`x_\delta, \delta \in \mathcal{C}^*`
and :math:`x_\pi,  \pi \in {{\rm Aut}_{{\rm St}} \mathcal{P}}`.
The generators  :math:`x_\delta` generate the subgroup of diagonal
automorphisms of :math:`{{\rm Aut}_{{\rm St}} \mathcal{P}}`. 


The group :math:`N_{0}` is generated by :math:`N_{x0}` and by 
another element :math:`\tau` of :math:`N_{0}` or order ``3``. The
group :math:`G_{x0}` is generated by :math:`N_{x0}` and by another
element  :math:`\xi` of :math:`G_{x0}` or order ``3``. The elements
:math:`x_\delta`, :math:`x_\pi`, :math:`x_e`, 
:math:`y_e`, :math:`z_e`,  :math:`\tau` and  :math:`\xi`  
generate the monster group  :math:`\mathbb{M}`.
In this  package we use the definitions of the generators 
in  :cite:`Seysen20`, which incorporate a modification of 
:cite:`Con85` made in :cite:`Iva09`. 
This leads to simpler relations in  :math:`N_{0}`.
The generators :math:`x_e`, :math:`y_e`, and :math:`z_e` in  
:cite:`Seysen20` correspond to the generators
:math:`x_e \cdot z_{-1}^{|e/4|}`, :math:`y_e \cdot x_{-1}^{|e/4|}`,
and  :math:`z_e \cdot y_{-1}^{|e/4|}` in :cite:`Con85`.
 

Representing elements of the monster group
..........................................

An element of the monster group :math:`\mathbb{M}` is represented 
as an instance of class ``MM`` in module ``mmgroup``.

Elements of the monster group are created by the constructor
of class |MM|. Usually, the constructor of class |MM| takes two
arguments ``tag`` and ``i``, where ``tag`` is a single small 
letter describing the type of the generator of :math:`\mathbb{M}`, 
and ``i`` is an integer describing the value of that generator. 
Alternatively, ``i`` may be an instance of the appropriate algebraic 
structure used for indexing a generator of a given type as 
indicated in the table below.


Implementation of the generators of the monster group
.....................................................


Math papers may use (at least) Latin or Greek letters for labelling
objects, but most programming languages are restricted to ASCII characters.
The following table shows how to create generating of the monster group
using the constructor of class |MM|:


.. table:: Construction of generating elements of the monster
  :widths: 10 90


  ===================  ==========================================================
  Element              Construction as an instance of class ``MM``, 
  ===================  ==========================================================
  :math:`x_\delta`     ``MM('d', delta)``, ``delta`` an instance of class
                       |Cocode|; 

                       ``MM('d', delta)`` returns 
                       ``MM('d', Cocode(delta))`` for ``0 <= delta < 0x1000``. 

  :math:`x_\pi`        ``MM(pi)``, ``pi`` an instance of class |AutPL|;

                       ``MM('d', delta) * MM('p', n)`` is equivalent to 
                       ``MM(AutPL(delta, n))`` 
                       for ``0 <= delta < 0x1000``, ``0 <= n < 244823040`` .

  :math:`x_e`          ``MM('x', e)``, ``x`` an  instance of class |PLoop|;

                       ``MM(('x', e))`` returns ``MM('x', PLoop(e))`` for
                       ``0 <= e < 0x2000``.

  :math:`y_e`          ``MM('y', e)``,  ``e`` as in case :math:`x_e`. 

  :math:`z_e`          ``MM('z', e)``,  ``e`` as in case :math:`x_e`. 

  :math:`\tau^e`       ``MM('t', e)``, exponent  ``e`` is an integer 
                       which is taken modulo ``3``.

  :math:`\xi^e`        ``MM('l', e)``,  exponent  ``e`` is an integer 
                       which is taken modulo ``3``.
  ===================  ==========================================================


More possibilities for constructing elements of an instance of class 
|MM| are given in the description of that class. Multiplication and 
exponentiation of group elements works a usual.  


Multiplication of elements of the monster group
...............................................

Internally, an element of :math:`\mathbb{M}` is represented as a word
of the generators given above. Multiplication with the ``*`` operator 
is a concatenation of such words, followed by a reduction step.
Multiplication of two reduced elements of the monster group (including
the reduction of the result) takes less than 50 milliseconds on the
author's computer. 

The reduction after a group operation is done by a new method that 
tracks pairs of perpendicular 2A axes, which at the moment is more a 
(yet undocumented) art than a science. This new method will be 
documented in a future version of the project. 

The verification of the result of a reduction is along the lines 
of the method given in :cite:`LPWW98`; for more details see section 
:ref:`check_equality_monster`. So even if you don't trust in the new
reduction method, the reduction algorithm is still of Las Vegas type; 
i.e. it never fails without indication. But in practice the new
algorithm is deterministic and always successful; and it has been 
tested on thousends of group operations.
"""
# References in the __docstr__ see file docs/source/references.bib


from __future__ import absolute_import, division, print_function
from __future__ import  unicode_literals



import sys
import os
import collections
import re
import warnings
from numbers import Integral
import numpy as np
from random import randint, sample


from mmgroup.generators import rand_get_seed, gen_leech2_type
from mmgroup.generators import gen_rng_modp
from mmgroup.structures.parse_atoms import ihex, TaggedAtom
from mmgroup.structures.mm0_group import MM0
from mmgroup.structures.abstract_group import singleton
from mmgroup.structures.abstract_mm_group import AbstractMMGroup
from mmgroup.structures.parse_atoms import  AtomDict
from mmgroup.structures.construct_mm import load_group_name     
from mmgroup.structures.construct_mm import iter_mm       
from mmgroup.generators import gen_leech2_type
from mmgroup.generators import gen_leech2_reduce_type4
from mmgroup.generators import mm_group_invert_word
from mmgroup.clifford12 import xsp2co1_check_word_g_x0 
from mmgroup.clifford12 import xsp2co1_reduce_word      
from mmgroup.clifford12 import xsp2co1_traces_all      
from mmgroup.clifford12 import chk_qstate12
from mmgroup.clifford12 import xsp2co1_rand_word_G_x0
from mmgroup.clifford12 import xsp2co1_rand_word_N_0
from mmgroup.mm import mm_vector



try:
    from mmgroup import mat24
    from mmgroup.mat24 import MAT24_ORDER, pow_ploop, ploop_theta
except (ImportError, ModuleNotFoundError):
    from mmgroup.dev.mat24.mat24_ref import Mat24  
    mat24 = Mat24  
    MAT24_ORDER = Mat24.MAT24_ORDER
    pow_ploop = Mat24.pow_ploop
    ploop_theta = Mat24.ploop_theta
    del Mat24


from mmgroup.structures.ploop import Cocode, PLoop
from mmgroup.structures.autpl import StdAutPlGroup, autpl_from_obj, AutPL

from mmgroup.generators import mm_group_mul_words






###########################################################################
# Import functions from module ``mmgroup.mm_order`` on demand
###########################################################################


# Functions to be imported from module mmgroup.mm_order
check_mm_order = None
check_mm_equal = None
check_mm_half_order = None
check_mm_in_g_x0 = None
mm_op15_reduce_M = None

def import_mm_order_functions():
    """Import functions from module ``mmgroup.mm_order``.

    We import these functions from module ``mmgroup.mm_order``
    on demand. This avoids an infinite recursion of imports.
    """
    global check_mm_order, check_mm_equal
    global check_mm_half_order, check_mm_in_g_x0
    global mm_op15_reduce_M
    from mmgroup.mm_order import check_mm_order as f
    check_mm_order = f
    from mmgroup.mm_order import check_mm_equal as f
    check_mm_equal = f
    from mmgroup.mm_order import check_mm_half_order as f
    check_mm_half_order = f
    from mmgroup.mm_order import check_mm_in_g_x0 as f
    check_mm_in_g_x0 = f
    from mmgroup.mm_order import compute_order_vector
    compute_order_vector()
    from mmgroup.mm15 import op_reduce_M as f
    mm_op15_reduce_M = f





###########################################################################
# Word class for the group MM
###########################################################################





class MM(MM0):
    r"""Models an element of the monster group :math:`\mathbb{M}`

    Let ``g1`` and ``g2`` be instances of class  |MM| representing 
    elements of the monster group.  Then
    ``g1 * g2``  means group multiplication, and ``g1 ** n`` means
    exponentiation of ``g1`` with the integer ``n``. ``g1 ** (-1)`` 
    is the inverse of ``g``. ``g1 / g2`` means ``g1 * g2 ** (-1)``.
    We have ``1 * g1 == g1 * 1 == g1`` and ``1 / g1 == g1 ** (-1)``.

    ``g1 ** g2`` means ``g2**(-1) * g1 * g2``.   

    Let ``V`` be a vector space that is a representation of ``MM``,
    see class |MMVector| for details. An instance ``g1`` of 
    class ``MM`` operates on the vector space  ``V`` by right 
    multiplication.  

    :var tag:
        In the simplest case, parameter ``tag`` is a string of length 
        ``1`` that determines the type of the atomic group element. 
        There are also some special cases for parameter ``tag `` as
        indicated below. If ``tag`` is not given or equal to ``1`` 
        then  the neutral element of the monster group is constructed.

     
    :var i:
        Parameter ``i`` is number of the atomic element of a given ``tag``.
        Depending on the tag, ``i`` may be the number of an element of one 
        of the structures |PLoop|, |Cocode|, or the number of an element of 
        the Mathieu  group ``M_24``, as explained in class |AutPL|.
        An element :math:`\pi` of the group |AutPL| is mapped to the
        element :math:`x_\pi` of the Monster group.
        
        The number ``i`` may also be an instance of the appropriate class
        |PLoop|, |Cocode|, or |AutPL|, as indicated in the table below.

    :return: An element of the monster group 
    :rtype:  an instance of class |MM|



    **Standard tags**

    The tags listed in the following tables are standard tags that can
    be used for creating generators (or some short words of generators)
    of the monster group.
 

    .. table:: Atomic elements of the Monster group
          :widths: 8 20 72

          +-------+-----------------+----------------------------------------+
          | Tag   | Number  ``i``   | Type of element                        |
          +=======+=================+========================================+
          |``'p'``| ``0-244823039`` | The automorphism ``AutPL(0, i)`` of    |
          |       |                 | the Parker loop, see below.            |
          +-------+-----------------+----------------------------------------+
          |``'d'``| ``0-0xfff``     | The diagonal automorphism ``Cocode(i)``|
          |       |                 | in |AutPL|.                            |
          +-------+-----------------+----------------------------------------+
          |``'x'``| ``0-0x1fff``    | The element :math:`x_e`,  with         |
          |       |                 | ``e = PLoop(i)``.                      |
          +-------+-----------------+----------------------------------------+
          |``'y'``| ``0-0x1fff``    | The element :math:`y_e`,               |
          |       |                 | ``e = PLoop(i)``;                      |
          |       |                 | similar to tag ``'x'``.                |
          +-------+-----------------+----------------------------------------+
          |``'z'``| ``0-0x1fff``    | The element :math:`z_e`,               |
          |       |                 | ``e = PLoop(i)``;                      |
          |       |                 | similar to tag ``'x'``.  We have       |
          |       |                 | :math:`x_e y_e z_e = y_e x_e z_e = 1`. |
          +-------+-----------------+----------------------------------------+
          |``'t'``| ``0-2``         | The element :math:`\tau^i`,            |
          +-------+-----------------+----------------------------------------+
          |``'l'``| ``0-2``         | The element :math:`\xi^i`,             |
          +-------+-----------------+----------------------------------------+
          |``'q'``| ``0-0x1ffffff`` | Describes an element of the subgroup   |
          |       |                 | :math:`Q_{x0}`. See remark below.      |
          +-------+-----------------+----------------------------------------+
          |``'c'``| ``0-0xffffff``  | A representative of a right coset of   |
          |       |                 | :math:`N_{x0}` in :math:`G_{x0}`.      |
          |       |                 | See remark below.                      |
          +-------+-----------------+----------------------------------------+


    Apart from the standard tags there are also some tags for
    special purposes discussed in the following sections.

    Remarks
          
    If ``i`` is the string ``'r'`` then a random element with the   
    given tag is generated.  If ``i`` is the string ``'n'`` then
    a random element with the given tag is generated, which is 
    different from the neutral element with a very high 
    probability.

    If ``tag == 'd'`` then  ``i = 'o'`` generates a random odd 
    and ``i = 'e'`` generates a  random even diagonal automorphism.
    In this case `i`` may also be an instance of class |Cocode|, 
    representing the diagonal automorphism correspnding to the
    given element of the Golay cocode.   
        
    If ``tag == 'p'`` then ``i`` may also be an instance of class 
    |AutPL|. Then the returned atom is the Parker loop automorphism
    given by that instance. If ``i`` is an integer then the Parker 
    loop  automorphism ``AutPL(0, i)`` is returned. This 
    automorphism is the standard rpresentative of the i-th element 
    of the  Mathieu group ``M_24`` in the automorphism group of the 
    Parker loop.

    If ``tag`` is ``'x'``,   ``'y'`` or ``'z'`` then ``i`` 
    may also be an instance of class |PLoop|, representing an 
    element of the Parker loop. 

    The exponent ``i`` for a tag ``'t'`` or ``'l'`` is reduced
    modulo ``3``. 

    The tag ``'q'`` is useful for encoding an element of the 
    subgroup :math:`Q_{x0}` of the monster. An atom with 
    tag ``'q'`` and index ``i``  encodes the element 
    :math:`x_d \cdot x_{\delta} \cdot x_{\theta(d)}`, 
    with :math:`d` = ``PLoop(i >> 12)`` :math:`\in \mathcal{P}``,   
    :math:`\delta` = ``Cocode(i & 0xfff)`` 
    :math:`\in \mathcal{C}^*`,  
    and   :math:`\theta: \mathcal{P} \rightarrow \mathcal{C}^*`
    the cocycle of the Parker loop.

    The tag ``'c'`` with index ``i`` encodes a representative
    of the right coset :math:`N_{x0} g, g \in G_{x0}` of  
    :math:`N_{x0}` in :math:`G_{x0}` that maps the standard
    frame  :math:`\Omega` in the Leech lattice modulo 2 to 
    a type-4 vector given by the index ``i``.
    Here ``i`` encodes a vector in the Leech lattice modulo 2
    as in the description for tag  ``'q'``. That vector must
    be of type 4. The sign bit of that vector is ignored.


    **Generating a random element of the subgroup of the monster**
 
    If parameter ``tag`` is equal to the string ``'r'`` then parameter 
    ``'i'`` should be a string describing a subgroup of the 
    monster group. Then a uniform distributed element from that
    subgroup is generated. The follwing subgroups are recognized:

    .. table:: Subgroups of the Monster group recognized
          :widths: 15 85

       +----------------+---------------------------------------------+
       | Parameter ``i``| Subgroup                                    | 
       +----------------+---------------------------------------------+
       | ``'M'``        | The monster group itself                    |
       +----------------+---------------------------------------------+
       | ``'G_x0'``     | Subroup  ``'G_x0'`` generated by            |
       |                | :math:`x_d, x_\delta, y_d, x_\pi, \xi`      |
       +----------------+---------------------------------------------+
       | ``'N_0'``      | Subroup  ``'N_0'`` generated by             |
       |                | :math:`x_d, x_\delta, y_d, x_\pi, \tau`     |
       +----------------+---------------------------------------------+
       | ``'N_x0'``     | Subroup  ``'N_x0'`` generated by            |
       |                | :math:`x_d, x_\delta, y_d, x_\pi`           |
       +----------------+---------------------------------------------+
       | ``'N_0_e'``    | Subroup of ``'N_0'`` of index 2 generated   |
       |                | by :math:`x_d, x_\delta, y_d, x_\pi, \tau`, |
       |                | :math:`\delta` even                         |
       +----------------+---------------------------------------------+
       | ``'N_x0_e'``   | Subroup of ``'N_x0'`` of index 2 generated  |
       |                | by :math:`x_d, x_\delta, y_d, x_\pi`,       |
       |                | :math:`\delta` even                         |
       +----------------+---------------------------------------------+

    Subgroup ``'G_x0'`` has structure :math:`2^{1+24}.\mbox{Co}_1`, and
    subgroup ``'N_0'`` has structure :math:`2^{2+11+22}.\mbox{M}_{24}`.
    ``'N_x0'`` is a subgroup of ``'N_0'`` of index 3.

    If Parameter ``i`` is an positive integer then an element of the
    monster of shape :math:`g_0 t_1 g_1 t_2 g_2 ... t_i g_i` is created,
    where :math:`g_j` is a random element of  ``'G_x0'``, and :math:`t_j` 
    is  :math:`\tau^{\pm 1}`.


    **Generating an element of monster from its internal representation**

    If parameter ``tag`` is equal to the string ``'a'`` then parameter 
    ``'i'`` should be an array-like object containing the
    internal representation of an element of the monster group.
 
    Internally, an element of the monster group is represented
    as an array of unsigned 32-bit integers, where each entry
    of the array describes a generator. See section
    :ref:`header-mmgroup-generators-label` for details.


    **Special types accepted as tags**
  
    In the simplest case the argument ``tag`` in the constructor is
    a string of length ``1``. There are a few other types which are
    also accepted as tags. For such a special tag, the following
    parameter ``i`` in the constructor is ignored. 

    Especially, we may encode a word of standard generators as a 
    list of tuples as indicated in the table below.

    .. table:: Legal types as tags in the constructor of class ``MM``
      :widths: 25 75

      +---------------------+-------------------------------------------+
      | Object of type      | Evaluates to                              |
      +=====================+===========================================+
      | type ``list``       | A list represents the product of its      |
      |                     | entries in the given order. An entry      |
      |                     | ``MM(tag, i)`` can be abbreviated  to     |
      |                     | the tuple ``(tag, i)``.                   |
      +---------------------+-------------------------------------------+
      | class |PLoop|       | The Parker loop element :math:`d`         | 
      |                     | given by that object is mapped to         |
      |                     | :math:`x_d \in \mathbb{M}`.               |
      +---------------------+-------------------------------------------+
      | class |AutPL|       | The Parker loop automorphism :math:`\pi`  | 
      |                     | given by that object is mapped to         |
      |                     | :math:`x_\pi \in \mathbb{M}`.             |
      +---------------------+-------------------------------------------+
      | class |Cocode|      | The Golay cocode element :math:`\delta`   |
      |                     | given by that object is mapped to         |
      |                     | :math:`x_\delta \in \mathbb{M}`.          |
      +---------------------+-------------------------------------------+
      | class |XLeech2|     | The element corresponding to that element |
      |                     | of  :math:`Q_{x0}` is created.            |
      +---------------------+-------------------------------------------+
      | class |MM|          | A deep copy of the given element of       | 
      |                     | :math:`\mathbb{M}` is made.               |
      +---------------------+-------------------------------------------+
      | ``str`` of length   | For an instance ``g`` of class ``MM``     |
      | greater than ``1``  | we have ``MM(str(g)) == g``.              |
      |                     |                                           |
      |                     | So we can reread                          |
      |                     | printed elements of ``MM``.               |
      +---------------------+-------------------------------------------+


    """
    MIN_LEN = 128
    __slots__ =  "length", "_data", "reduced"
    def __init__(self,  tag = None, i = None, *args, **kwds):
        self.reduced = 0
        atoms = iter_mm(self.group, tag, i)
        self._data = np.fromiter(atoms, dtype = np.uint32) 
        self.length = len(self._data)
        self._extend(self.MIN_LEN)
        self.reduce()

    def _t_shape(self):
        l = []
        self.reduce()
        for d in self.mmdata:
            tag = (d >> 28) & 7
            if tag == 5: l.append('T')
            if tag == 6: l.append('x')
        return "<" + "".join(l) + ">"




###########################################################################
# The class representing the group MM
###########################################################################


@singleton
class MMGroup(AbstractMMGroup):
    r"""An instance of this class models the monster group as an object

    :param: None

    :return: An instance of the monster group 
    :rtype:  an instance of class |MMGroup|

    Class |MMGroup| is implemented as a singleton. Calling the constructor
    of that class always returns the same instance of that class. 

    Elements of the monster group are implemented as instances of class
    ``MM``. 
    """
    ERR_REDUCE = "Reduction in monster group failed"
    __instance = None
    word_type = MM
    group_name = "M"


    def __init__(self):
        """ TODO: Yet to be documented     


        """
        super(MMGroup, self).__init__()



    def reduce(self, g1, copy = False):
        l1 = g1.length
        if not g1.reduced:
            if not mm_op15_reduce_M:
                import_mm_order_functions() 
            if copy:
                g2 = self.word_type()
                length = mm_op15_reduce_M(g1._data, g1.length, g2._data)
                if not 0 <= length <= 128:
                    raise ValueError(self.ERR_REDUCE)
                g2.length = length
                g2.reduced = True
                return g2
            else:
                a = np.zeros(128, dtype = np.uint32)
                length = mm_op15_reduce_M(g1._data, g1.length, a)
                if not 0 <= length <= 128:
                    raise ValueError(self.ERR_REDUCE)
                g1._setdata(a[:length])
                g1.reduced = True
                return g1
        return self.copy(g1) if copy else g1

        
    def _imul(self, g1, g2):
        l1, l2 = g1.length, g2.length
        g1._extend(2*(l1 + l2) + 1)
        g1._data[l1 : l1 + l2] = g2._data[:l2]
        l1 += l2
        g1.length = l1
        g1.reduced = False
        g1.reduce()
        return g1

    def _invert(self, g1):
        w = self.word_type()
        w._setdata(np.flip(g1.mmdata) ^ 0x80000000)
        w.reduced = False
        return w

    def copy_word(self, g1):
        result = self.word_type()
        result._setdata(g1.mmdata)
        result.reduced = g1.reduced
        return result

    def _equal_words(self, g1, g2):
        if not check_mm_equal is None:
            return g1.group == g2.group and check_mm_equal(g1, g2)
        try:
            import_mm_order_functions()
            return g1.group == g2.group and check_mm_equal(g1, g2)
        except:
            if g1.group != g2.group:
                return False
            g1.reduce()
            g2.reduce()
            if (g1.mmdata == g2.mmdata).all():
                 return True
            raise ValueError("Don't know if monster group elements are equal")

    def str_word(self, g):
        try:
            g.reduce()
        except:
            pass
        return super(MMGroup, self).str_word(g)



StdMMGroup = MMGroup()
MM.group = StdMMGroup
load_group_name(StdMMGroup, "M")



