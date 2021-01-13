r"""

The functions in file ``gen_leech.c`` implement the operation of the
subgroup :math:`G_{x0}` (of structure :math:`2^{1+24}.\mbox{Co}_1`)
of the monster group on its extraspecial subgroup :math:`Q_{x0}` 
(of structure :math:`2^{1+24}`) by conjugation.

Here an element of the group :math:`Q_{x0}` is given as a 25-bit 
integer in Leech lattice encoding. From that encoding we obtain an 
encoding of :math:`\Lambda / 2 \Lambda` (where :math:`\Lambda` is 
the Leech lattice) by dropping the most significant bit. This 
corresponds to the isomorphism
:math:`Q_{x0} / \{\pm1\} \cong \Lambda / 2 \Lambda`.

An element of the group  :math:`G_{x0}` is encoded as an array of 
32-bit integers, where each integer corresponds to a generator of
the group, as described in the documentation of the header file
``mmgroup_generators.h``.
  
A vector in the Leech lattice modulo 2 has a type and also a subtype
as described in **The mmgroup guide for developers**, section
:ref:`computation-leech2`. Here the subtype is a two-digit decimal
number, where the first digit is the type. Function 
``gen_leech2_type`` returns the subtype as a BCD-coded integer.
E.g. the subtype 46 is returned as the hexadecimal integer 0x46. 
So the type can be obtained from the subtype via a shift operation.

For computations in the group :math:`G_{x0}` or :math:`\mbox{Co}_1`
it is important to find an element of :math:`G_{x0}` that maps an 
arbitrary type-4 vector in :math:`\Lambda / 2 \Lambda` to the unique
type-4 vector :math:`\Omega`, see :ref:`computation-leech2`.
Function ``gen_leech2_reduce_type4`` performs this task.

The construction of the group :math:`G_{x0}` also requires some
computations in the automorphism group :math:`\mbox{Co}_0`
(of structure :math:`2.\mbox{Co}_1`) of  :math:`\Lambda`, see
:cite:`Con85`, section 9 or :cite:`Seysen20`, section 9. The group
:math:`\mbox{Co}_0` acts faithfully on :math:`\Lambda / 3 \Lambda`. 
Therefore file ``gen_leech.c`` also provides some functions for 
dealing with vectors in the Leech lattice modulo 3.

For any :math:`w \in \Lambda` the vector 
:math:`v = \sqrt{8} \cdot w` has integral coordinates. We 
represent a vector :math:`w \in \Lambda / 3 \Lambda` by the vector  
:math:`v = \sqrt{8} \cdot w`, with the coordinates of :math:`v` 
taken modulo 3. We represent each coordinate 
:math:`v_i, 0 \leq i < 24` as a two-bit integer;
so all 48 bits of :math:`v` fit into the a 64-bit integer. Let
:math:`v_{i,1}, v_{i,0}` be the bits of :math:`v_{i}` of 
valence :math:`2^1` and :math:`2^0`, respectively. Then we
encode :math:`v` as an 48-bit integer :math:`x` so that bit 
:math:`24 \cdot j+i` of :math:`x` is equal to :math:`v_{i,j}`. 
This encoding looks peculiar, but it greatly simplifies the 
interaction with the functions in file ``mat24_functions.c``. We 
call this encoding the **Leech lattice mod 3** encoding.
On input, both bits :math:`v_{i,1}, v_{i,0}` may be equal to 1;
but on output, at most on of these bits is equal to 1. 

In :cite:`Seysen20`, section 9.3, the generators  
:math:`x_d, x_\delta, y_\delta, x_\pi, \xi` of :math:`G_{x0}`
are also defined as generators of a group  :math:`G_{x1}` with 
:math:`|G_{x1}:G_{x0}| = 2`. The group :math:`G_{x1}` operates
on :math:`\Lambda`, but the group :math:`G_{x0}` does not.
So we take these generators as generators of :math:`G_{x1}`.


"""
