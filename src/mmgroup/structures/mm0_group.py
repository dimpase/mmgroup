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
and  :math:`z_e \cdot y_{-1}^{|e/4|}`` in :cite:`Con85`.
 

Creating an instance of the monster group
.........................................


For dealing with the monster group :math:`\mathbb{M}` the user must 
first create an instance ``MM`` of class |MMGroup|, which 
represents the monster group :math:`\mathbb{M}`::

      MM = MMGroup()


Class |MMGroup| is implemented as a singleton. Calling the constructor
of that class always returns the same instance of that class. There is
the predefined instance ``mmgroup.MM`` of class |MMGroup|.

Elements of the monster group are created by calling that instance ``MM`` 
as a function with a variable number of arguments. Here each argument 
describes an element of :math:`\mathbb{M}` which is (usually) one of the 
generators listed above. The the function returns the product of all 
these elements as an instance of class |MMGroupWord|. Instances of class  
|MMGroupWord| model elements of the Monster group :math:`\mathbb{M}`.

An argument passed to an instance ``MM`` of class  |MMGroup| may be a pair 
``(tag, value)``, where ``tag`` is a single small letter describing the 
type of the generator of :math:`\mathbb{M}`, and ``value`` is an 
integer describing the value of that generator. Alternatively, ``value``
may be an instance of the appropriate algebraic structure used for
indexing a generator of a given type as indicated in the table below.


Implementation of the generators of the monster group
.....................................................


Math papers may use (at least) Latin or Greek letters for labelling
objects, but most programming languages are restricted to ASCII characters.
Assuming that ``MM`` is an instance of class  |MMGroup| representing
a monster group, the following table shows how to create generating
elements of ``MM``: 


.. table:: Construction of generating elements of the monster
  :widths: 10 90


  ===================  ==========================================================
  Element              Construction as an element of ``MM``, 
                       with ``MM`` of type |MMGroup|
  ===================  ==========================================================
  :math:`x_\delta`     ``MM(('d', delta))``, ``delta`` an instance of class
                       |Cocode|; 

                       ``MM(('d', delta))`` returns 
                       ``MM('d', Cocode(delta))`` for ``0 <= delta < 0x1000``. 

  :math:`x_\pi`        ``MM(pi)``, ``pi`` an instance of class |AutPL|;

                       ``MM(('d', delta), ('p', n))`` returns 
                       ``MM(AutPL(delta, n))`` 
                       for ``0 <= delta < 0x1000``, ``0 <= n < 244823040`` .

  :math:`x_e`          ``MM(('x', e))``, ``x`` an  instance of class |PLoop|;

                       ``MM(('x', e))`` returns ``MM(('x', PLoop(e)))`` for
                       ``0 <= e < 0x2000``.

  :math:`y_e`          ``MM(('y', e))``,  ``e`` as in case :math:`x_e`. 

  :math:`z_e`          ``MM(('z', e))``,  ``e`` as in case :math:`x_e`. 

  :math:`\tau^e`       ``MM(('t', e))``, exponent  ``e`` is an integer 
                       which is taken modulo ``3``.

  :math:`\xi^e`        ``MM(('l', e))``,  exponent  ``e`` is an integer 
                       which is taken modulo ``3``.
  ===================  ==========================================================


More possibilities for constructing elements of an instance of class 
|MMGroup| are given in the description of that class. An element ``g``
of an instance of the monster group is modelled as in instance of class 
|MMGroupWord|. ``g.group`` is the group where ``g`` belongs to; that 
group is an instance of class |MMGroup|. Multiplication and 
exponentiation of group elements works a usual.  


Multiplication of elements of the monster group
...............................................

Internally, an element of  :math:`\mathbb{M}` is represented as a word
in the generators given above. The user should be aware of the fact
that multiplication with the ``*`` operator is a concatenation of such
words, followed by (rather incomplete) reduction step. This means that 
multplying words may still lead to an exponential growth of the word 
length. 

On can apply the method ``simplify`` to an element of the monster group.
This method shortens a word representing an element of :math:`\mathbb{M}`
to a reasonable length with a very high probability. However, applying 
this method usually takes a long time. On the author's computer it may 
take several minutes to shorten the product of two (previously shortened) 
random words. This is yet considerably faster than the run time reported 
in :cite:`Wilson13`.

In such a word we always reduce substrings of generators of the 
subgroup :math:`N_0` of :math:`\mathbb{M}` to a standard form, 
which is easy. We apply no relations to the remaining generator
:math:`\xi`, except for :math:`\xi^3=1`. Method ``simplify`` uses
the technique described in :cite:`Wil03` for shortening a word
in the monster group.




Future development
..................

Future versions of this package may implement improved reduction
strategies for words of generators of :math:`\mathbb{M}` :


 * Long words of generators of :math:`\mathbb{M}` can be shortened 
   with high probability by method ``mmgroup.MMGroupWord.simplify``. 
   This method uses the algorithm in :cite:`Wil03`. This may take 
   a long time. Here improvements in future versions are desirable.

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


from mmgroup.generators import rand_get_seed
from mmgroup.generators import gen_rng_modp
from mmgroup.structures.parse_atoms import ihex, TaggedAtom
from mmgroup.structures.abstract_group import singleton
from mmgroup.structures.abstract_mm_group import AbstractMMGroupWord
from mmgroup.structures.abstract_mm_group import AbstractMMGroup
from mmgroup.structures.parse_atoms import  AtomDict
from mmgroup.structures.construct_mm import iter_mm       
from mmgroup.structures.construct_mm import load_group_name     
from mmgroup.generators import gen_leech2_reduce_type4
from mmgroup.generators import mm_group_invert_word
from mmgroup.clifford12 import xsp2co1_check_word_g_x0 
from mmgroup.clifford12 import xsp2co1_reduce_word      
from mmgroup.clifford12 import xsp2co1_traces_fast      
from mmgroup.clifford12 import chk_qstate12
from mmgroup.clifford12 import xsp2co1_rand_word_G_x0
from mmgroup.clifford12 import xsp2co1_rand_word_N_0
from mmgroup.mm import mm_vector



try:
    from mmgroup.mat24 import MAT24_ORDER, pow_ploop, ploop_theta
except (ImportError, ModuleNotFoundError):
    from mmgroup.dev.mat24.mat24_ref import Mat24    
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

def import_mm_order_functions():
    """Import functions from module ``mmgroup.mm_order``.

    We import these functions from module ``mmgroup.mm_order``
    on demand. This avoids an infinite recursion of imports.
    """
    global check_mm_order, check_mm_equal
    global check_mm_half_order, check_mm_in_g_x0
    global mm_reduce_M
    from mmgroup.structures.mm_order import check_mm_order
    from mmgroup.structures.mm_order import check_mm_equal 
    from mmgroup.structures.mm_order import check_mm_half_order
    from mmgroup.structures.mm_order import check_mm_in_g_x0




###########################################################################
# Import functions from module ``mmgroup.structures.xsp2_co1`` on demand
###########################################################################


# Functions to be imported from modules mmgroup.structures.xsp2_co1
# and mmgroup.structures.involutions
Xsp2_Co1 = None
xsp2co1_to_mm = None
mm_conjugate_involution = None
reduce_via_power = None


def import_Xsp2_Co1():
    global Xsp2_Co1, xsp2co1_to_mm, mm_conjugate_involution
    global reduce_via_power
    from mmgroup.structures.xsp2_co1 import Xsp2_Co1 as f
    Xsp2_Co1 = f
    from mmgroup.structures.xsp2_co1 import Xsp2_Co1 as f
    xsp2co1_to_mm = f
    from mmgroup.structures.involutions import mm_conjugate_involution as f
    mm_conjugate_involution = f    
    from mmgroup.structures.involutions import reduce_via_power as f
    reduce_via_power = f


###########################################################################
# Word class for the group MM0
###########################################################################





class MM0(AbstractMMGroupWord):
    r"""Models an element of the monster group :math:`\mathbb{M}`

    Let ``MM`` be an instance of class ``MMGroup``, and let ``g1``, 
    ``g2`` be elements of ``MM``.  Then
    ``g1 * g2``  means group multiplication, and ``g1 ** n`` means
    exponentiation of ``g1`` with the integer ``n``. ``g1 ** (-1)`` 
    is the inverse of ``g``. ``g1 / g2`` means ``g1 * g2 ** (-1)``.
    We have ``1 * g1 == g1 * 1 == g1`` and ``1 / g1 == g1 ** (-1)``.

    ``g1 ** g2`` means ``g2**(-1) * g1 * g2``.   

    Let ``V`` be a vector space that is a representation of ``MM``,
    see class |MMSpace| for details. An element ``g1`` of ``MM`` 
    operates on the vector space  ``V`` by right multiplication.  

    :var group:
        This attribute contains the group to which the element belongs.
        That group is an instance of class |MMGroup|.

    .. warning::
       The constructor of this class is not for public use! You
       may call an instance ``MM`` of class  |MMGroup| for
       constructing elements of the instance ``MM`` of the monster 
       group.
  
    """
    __slots__ =  "length", "_data", "reduced"
    ERR_ITER = "A monster group element g is not iterable. Use g.mmdata instead"
    MIN_LEN = 16
    def __init__(self,  tag = None, atom = None, *args, **kwds):
        if tag is None:
            self._data = np.zeros(self.MIN_LEN, dtype = np.uint32) 
            self.length = 0
            self.reduced = 1
        else:
            self.reduced = 0
            atoms = iter_mm(self.group, tag, atom)
            self._data = np.fromiter(atoms, dtype = np.uint32) 
            self.length = len(self._data)
            if self.length < self.MIN_LEN:
                self._data = np.resize(self._data, self.MIN_LEN)
                  
    def _extend(self, length):
        if length > len(self._data):
            length = max(length, 3*len(self._data) >> 1)
            self._data = np.resize(self._data, length)
              
    @property
    def mmdata(self):
        """Return the internal representation of the group element

        Internally, an element of the monster group is represented
        as an array of unsigned 32-bit integers, where each entry
        of the array describes a generator. See section
        :ref:`header-mmgroup-generators-label` for details.
        """
        self.reduce()
        return np.copy(self._data[:self.length])


    def __bool__(self):
        return True
        
    def __len__(self):
        raise TypeError(self.ERR_ITER)

    def _setdata(self, data):
        self.length = len_ = len(data)
        self._extend(len_)
        self._data[:len_] = data
        self.reduced = False

        
    def __getitem__(self,i):
        raise TypeError(self.ERR_ITER)
 
        
    def is_reduced(self):
        """Return ``True`` if the element of the monster group is reduced

        An element ``g`` of the monster group represented by an instance
        of this class may be reduced by calling
        ``g.reduce()``.
        """
        return self.length == self.reduced




    def order(self, max_order = 119):
        r"""Return the order of the element of the monster group

        We use the method in :cite:`LPWW98`, section 7, for computing
        the order of an element of the monster.

        If the argument ``max_order`` is present then the order of the 
        element is checked up to (and including) ``max_order`` only.  
        Then the function returns ``0`` if the order is greater than 
        ``max_order``. By default, the function returns the exact 
        order of the element.
        """
        if check_mm_order is None:
            import_mm_order_functions()
        self.reduce()
        return check_mm_order(self, max_order)

    def half_order(self, max_order = 119):
        r"""Return the (halved) order of the element of the monster group

        The function  returns a pair ``(o, h)``, where ``o`` is the 
        order of the element.

        If ``o`` is even then the function returns the pair ``(o, h)``,
        where ``h`` is the element raised to to the ``(o/2)``-th power. 
        Otherwise the function returns the pair ``(o, None)``.
   
        Parameter ``max_order`` is as in function ``check_mm_order``. 

        If ``h`` is in the subgroup :math:`G_{x0}`` then ``h`` is 
        returned as a word in the generators of that subgroup.
        """
        if check_mm_half_order is None:
            import_mm_order_functions()
        self.reduce()
        return check_mm_half_order(self, max_order)

    def in_G_x0(self):
        r"""Check if the element is in the subgroup :math:`G_{x0}`

        The function returns True if this is the case. If this is
        the case then the element is converted to a word in the
        generators of :math:`G_{x0}`.

        This method uses geometric information about the Leech 
        lattice taken from :cite:`Iva99`.
        """
        self.reduce()
        if check_mm_in_g_x0 is None:
            import_mm_order_functions()
        return check_mm_in_g_x0(self) is not None
                          
    def chi_G_x0(self, involution = None):
        r"""Compute characters of element of subgroup :math:`G_{x0}`

        If the element is in the subgroup :math:`G_{x0}` then the 
        function returns a tuple 
        :math:`(\chi_M, \chi_{299}, \chi_{24}, \chi_{4096})`
        of integers. Otherwise it raises ``ValueError``.

        Here :math:`\chi_M` is the character of the element in the
        196833-dimensional rep :math:`198883_x` of the monster.

        By Conway's construction of the monster we have:

        :math:`198883_x =  299_x \oplus 24_x \otimes  4096_x
        \oplus 98280_x`,

        for suitable irreducible representations 
        :math:`299_x, 24_x, 4096_x, 98280_x` of the group 
        :math:`G_{x0}`. The corresponding characters of the
        element of  :math:`G_{x0}` are returned in the tuple
        given above.  

        While the product :math:`\chi_{24} \cdot \chi_{4096}`
        is well defined, the factors  :math:`\chi_{24}` and 
        :math:`\chi_{4096}` are defined up to sign only. We
        normalize these factors such that the first nonzero value 
        of the pair :math:`(\chi_{24}, \chi_{4096})` is positive. 

        If parameter ``involution`` is a 2B involution :math:`i` then
        the element :math:`g` given by ``self`` must centralize that
        involution  :math:`i`. In this case we compute the  
        corresponding  characters of  :math:`g^h` for a  
        :math:`h \in \mathbb{M}` such that  :math:`i^h`  is the
        central involution of :math:`G_{x0}`.
        """
        if involution:
             _, h = involution.conjugate_involution()
             g = self**h
             if g.in_G_x0() is None:
                 err = "Element does not centralize the given 2B involution"
                 raise ValueError(err)
        else:
             g = self
             if g.in_G_x0() is None:
                 err = "Element is not in the subgroup G_x0 of the monster"
                 raise ValueError(err)

        if Xsp2_Co1 is None: 
            import_Xsp2_Co1()
        elem = Xsp2_Co1(g)

        a = np.zeros(4, dtype = np.int32)
        res = chk_qstate12(xsp2co1_traces_fast(elem._data, a))
        chi24, chisq24, chi4096, chi98260 = map(int, a[:4])
        chi299 = (chi24**2 + chisq24) // 2 - 1
        chi_M = chi299 + chi98260 + chi24 * chi4096
        return chi_M, chi299, chi24, chi4096
       
    def in_N_x0(self):
        r"""Check if the element is in the subgroup :math:`N_{x0}`

        The function returns True if this is the case. If this is
        the case then the element is converted to a word in the
        generators of :math:`N_{x0}`.
        """
        if check_mm_in_g_x0 is None:
            import_mm_order_functions()
        if check_mm_in_g_x0(self) is None:
            return False
        self.reduce()
        for atom in self.mmdata:
            if ((atom >> 28) & 7) > 4:
                return False
        return True
 
    def in_Q_x0(self):
        r"""Check if the element is in the subgroup :math:`Q_{x0}`

        The function returns True if this is the case. If this is
        the case then the element is converted to a word in the
        generators of :math:`Q_{x0}`.
        """
        if check_mm_in_g_x0 is None:
            import_mm_order_functions()
        if check_mm_in_g_x0(self) is None:
            return False
        self.reduce()
        for atom in self.mmdata:
            if (atom & 0x70000000) not in [0x10000000,  0x30000000]:
                return False
        return True
             

    def conjugate_involution(self, check=True, ntrials=40, verbose=0):
        r"""Find an element conjugating an involution into the centre

        If the element :math:`g` given by ``self`` is an involution 
        in  the monster then the method computes an element :math:`h` 
        of the monster   with  :math:`h^{-1} g h = z`, where  
        :math:`z` is defined as follows:

        If :math:`g = 1`, we put :math:`h = z = 1`

        if :math:`g` is a 2A involution (in the monster) then we let
        :math:`z` be the involution in  :math:`Q_{x0}` corresponding 
        to the Golay cocode word with entries  :math:`2,3` being set.

        if :math:`g` is a 2B involution (in the monster) then we let 
        :math:`z` be the central involution in :math:`G_{x0}`

        The function returns a pair ``(I, h)``, where :math:`h` as an 
        element of the instance  ``MM`` of class ``MMGroup``. We put
        ``I = 0`` if :math:`g = 1`. We put ``I = 1, 2`` if 
        :math:`g` is a 2A or 2B involution, respectively.

        This function may take a long time. Parameter  ``ntrials``
        gives the number of trials to find a suitable element
        :math:`h`. Default is  ``ntrials = 40``. The function may
        fail after that number of trials even if the element is a
        2B involution.

        If parameter ``check`` is True (default) then the function 
        first checks if ``g`` is an involution.

        In future versions support for multiprocessing may be added.
        """
        self.reduce()
        if mm_conjugate_involution is None: 
            import_Xsp2_Co1()
        return mm_conjugate_involution(self, check, ntrials, verbose)


    def conjugate_involution_G_x0(self, guide = 0, group = None):
        """Wrapper for corresponding method in class ``mmgroup.Xsp2_Co1``

        Here ``self`` must be an involution :math:`g` in the subgroup
        :math:`G_{x0}` of the Monster.
        This function performs the same computation as the
        corresponding method in class ``mmgroup.Xsp2_Co1``. 
        It returns a pair ``(iclass, a)`` such that
        :math:`h = a^{-1} g a` is a (fixed) representative of 
        the class of :math:`g` in the  group :math:`G_{x0}`. Here 
        ``h`` is described by the integer ``iclass`` as documented 
        in the corresponding method mentioned above.

        If ``group`` is ``None`` (default) then ``a`` is an instance
        of the same class as ``g``.
        """ 
        self.reduce()
        if mm_conjugate_involution is None: 
            import_Xsp2_Co1()
        if group is None: group = self.__class__
        elem = Xsp2_Co1('a', self.mmdata)
        return elem.conjugate_involution_G_x0(guide, group)



    def half_order_chi(self,  ntrials=40):
        r"""Return order and some character information of the element

        The function  returns a triple ``(o, chi, h)``, where ``o`` is 
        the order of the element :math:`g` of the monster given 
        by ``self``. 

        If the order :math:`o` of  :math:`g` is odd then the triple 
        ``(o, None, None)`` is returned.

        If  the order of :math:`g` is even then we return the triple
        ``(o, chi, h)``. Here ``h`` is an element :math:`h` of
        :math:`\mathbb{M}` such that :math:`z = h^{-1} g^{o/2} h` is 
        the  standard 2A or 2B involution as in method
        ``conjugate_involution``.

        If :math:`g` powers up to a 2B involution then ``chi``
        is equal to the character of  :math:`u = h^{-1} g h`. 
        Here the character of the element :math:`u` of
        :math:`G_{x0}` is returned  as a quadruple as in method
        ``chi_G_x0``. 

        If :math:`g` powers up to a 2A involution then ``chi``
        is equal to to ``None``.
        """
        o, ho = self.half_order()
        chi, h = None, None
        if ho:
            _, h = ho.conjugate_involution(True, ntrials)
            try:
               chi = (self**h).chi_G_x0()
            except ValueError:
               chi = None
        return o, chi, h



    def simplify(self, ntrials=None, verbose=0):
        """Try to simplify an element of the monster group

        This function tries to simplify an element of the monster group.
        It may take a long time, but this is the only way to prevent the
        explosion of the word lengths of elements of the monster group. 

        The current version uses the word shortening algorithm
        in  :cite:`Wil03`. Parameter ``ntrials`` specifies the number
        of trials. Here the default value for ``ntrials`` should be
        used, since the parameter may be dropped in future versions.

        The word shortening algorithm and the implementation of this 
        method is experimental and may change in future versions!
        """
        if check_mm_in_g_x0 is None:
            import_mm_order_functions()
        check_mm_in_g_x0(self)
        self.reduce()
        weight = sum([((x >> 28) & 7) == 5 for x in self.mmdata])
        #print(weight)
        if weight <= 9:
             return self
        if ntrials is None:
            ntrials = 40
        else:
            w = ("The default value of parameter 'ntrials' should be used"
                 " in method mmgroup.MM.simplify")
            warnings.warn(w)
        if reduce_via_power is None:
            import_Xsp2_Co1()
        try: 
            g = reduce_via_power(self, ntrials, verbose = verbose)
            assert g == self
            self._setdata(g.mmdata)
            self.reduce()
        except:
            w = "Simplification of monster group element failed"
            warnings.warn(w)
        return self


###########################################################################
# The class representing the group MM
###########################################################################




@singleton
class MM0Group(AbstractMMGroup):
    r"""An instance ``MM`` of this class models an instance of the monster

    :param: None

    :return: An instance of the monster group 
    :rtype:  an instance of class |MMGroup|

    This means that ``MM = MMGroup()`` creates an instance ``MM`` of the 
    monster group  :math:`\mathbb{M}`. For generating an element ``g`` 
    of ``MM`` one must call ``MM`` as a function with a variable number 
    of arguments. Depending on its type, each argument is evaluated to
    an element of ``MM`` as indicated in the table below, and the
    product of these elements is returned. 

    Elements of the monster group are implemented as instances of class
    ``MMGroupWord``. The preferred way to construct an element of the 
    monster group is to call an instance of class |MMGroup|.  

    .. table:: Legal types for constructing an element of the monster
      :widths: 25 75

      +---------------------+-------------------------------------------+
      | Object of type      | Evaluates to                              |
      +=====================+===========================================+
      | tuple (``tag, i``)  | ``MM((tag, i))`` is equivalent to         |
      |                     | ``MM.atom(tag, i)``                       |
      +---------------------+-------------------------------------------+
      | class |PLoop|       | The Parker loop element :math:`d`         | 
      |                     | given by that object is mapped to         |
      |                     | :math:`x_d \in \mathbb{M}`                |
      +---------------------+-------------------------------------------+
      | class |AutPL|       | The Parker loop automorphism :math:`\pi`  | 
      |                     | given by that object is mapped to         |
      |                     | :math:`x_\pi \in \mathbb{M}`              |
      +---------------------+-------------------------------------------+
      | class |Cocode|      | The Golay cocode element :math:`\delta`   | 
      |                     | given by that object is mapped to         |
      |                     | :math:`x_\delta \in \mathbb{M}`           |
      +---------------------+-------------------------------------------+
      | class |MMGroupWord| | A deep copy of the given element of       | 
      |                     | :math:`\mathbb{M}` is made                |
      +---------------------+-------------------------------------------+
      | ``str``             | For an element ``g`` of ``MM`` we have    |
      |                     | ``MM(str(g)) == g``.                      |
      |                     |                                           |
      |                     | So we can reread                          |
      |                     | printed elements of ``MM``.               |
      +---------------------+-------------------------------------------+

    See class |MMGroupWord| for the group operation on an instance
    ``MM`` of  class |MMGroup|.

    Two elements ``g1, g2`` of the monster group can be tested for 
    equality with the ``==`` operator as usual. Here we use the 
    method given in :cite:`Wil03` for checking ``g1 * g2**(-1) == 1``.

    Elements ``g1``, ``g2`` that belong to different instances of
    class |MMGroup| are considered unequal.
    """
    word_type = MM0
    #STR_FORMAT = r"M<%s>"
    group_name = "M0"


    def __init__(self):
        """ TODO: Yet to be documented     


        """
        super(MM0Group, self).__init__()

    def reduce(self, g1):
        l1 = g1.length
        if g1.reduced < l1:
            l_tail = l1 - g1.reduced
            g1._extend(l1 + l_tail + 1)
            g1._data[l1 : l1 + l_tail] = g1._data[g1.reduced : l1]
            tail =  g1._data[l1:]
            l1 = mm_group_mul_words(g1._data, g1.reduced, tail, l_tail, 1)
            g1.reduced = g1.length = l1
        return g1

        
    def _imul(self, g1, g2):
        l1, l2 = g1.length, g2.length
        g1._extend(2*(l1 + l2) + 1)
        g1._data[l1 : l1 + l2] = g2._data[:l2]
        l1 += l2
        l_tail = l1 - g1.reduced
        g1._data[l1 : l1 + l_tail] = g1._data[g1.reduced : l1]
        tail = g1._data[l1:]
        l1 = mm_group_mul_words(g1._data, g1.reduced, tail, l_tail, 1)
        g1.reduced = g1.length = l1
        return g1

    def _invert(self, g1):
        w = self.word_type()
        w._setdata(np.flip(g1.mmdata) ^ 0x80000000)
        return self.reduce(w)

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



StdMM0Group = MM0Group()
MM0.group = StdMM0Group
load_group_name(StdMM0Group, "M0")




