We are given a long list of definitions from category theory and higher category theory. The task is to check each definition for accuracy. I will go through each term and compare the given definition with the standard mathematical definition. I will note any inaccuracies or missing details.
Note: Some terms might have variations in definition, but I will stick to the most common ones.
Let's start with the classical category theory part.
### Abelian category
**Given Definition:**
- A zero object,
- All binary products and coproducts,
- All kernels and cokernels,
- Every monomorphism is a kernel of some morphism, and every epimorphism is a cokernel of some morphism.
**Review:** This is standard. However, note that in many sources, the existence of all finite products and coproducts is required (not just binary). Also, the condition that every monomorphism is a kernel and every epimorphism is a cokernel is equivalent to the condition that every monomorphism is normal and every epimorphism is conormal. This definition is correct.
### Additive category
**Given Definition:** An Additive category is a preadditive category (i.e., enriched over the category Ab of abelian groups) that has all finite biproducts (products which are also coproducts).
**Review:** Correct. Note that in some older texts, additive categories might not require all finite biproducts, but the modern definition does.
### Adjoint functor theorem
**Given Definition:** The Adjoint Functor Theorem gives conditions under which a functor 
F
:
C
→
D
F:C→D has a left adjoint. In particular, if 
C
C is complete, locally small, and 
F
F preserves limits and satisfies the solution set condition, then 
F
F has a left adjoint.
**Review:** This is the Freyd Adjoint Functor Theorem. The conditions are correct. Note that the solution set condition is essential.
### Adjunction (unit, counit; left and right adjoints)
**Given Definition:** 
- Functors 
F
:
C
→
D
F:C→D, 
G
:
D
→
C
G:D→C,
- Natural transformations: Unit 
η
:
id
C
⇒
G
∘
F
η:id 
C
​
 ⇒G∘F, Counit 
ε
:
F
∘
G
⇒
id
D
ε:F∘G⇒id 
D
​
 ,
- Satisfying the triangle identities.
**Review:** Correct.
### Automorphism
**Given Definition:** An automorphism is an isomorphism from an object to itself.
**Review:** Correct.
### Balanced category
**Given Definition:** A balanced category is one in which every bimorphism (a morphism that is both monic and epic) is an isomorphism.
**Review:** Correct. Examples include Set and Abelian categories.
### Category (small, large, locally small)
**Given Definition:** 
- A collection of objects,
- For each pair of objects, a set (or class) of morphisms,
- Identity and associative composition.
It is **small** if both objects and hom-classes are sets; **large** otherwise; **locally small** if all hom-classes are sets.
**Review:** Correct. Note that in some foundations, "large" might be avoided, but the definitions are standard.
### Category of elements
**Given Definition:** For a presheaf 
F
:
C
op
→
S
e
t
F:C 
op
 →Set, the category of elements 
∫
F
∫F has objects pairs 
(
c
,
x
)
(c,x) with 
c
∈
C
c∈C, 
x
∈
F
(
c
)
x∈F(c), and morphisms 
f
:
(
c
,
x
)
→
(
d
,
y
)
f:(c,x)→(d,y) given by 
f
:
c
→
d
f:c→d such that 
F
(
f
)
(
y
)
=
x
F(f)(y)=x.
**Review:** Correct. Note that 
F
(
f
)
:
F
(
d
)
→
F
(
c
)
F(f):F(d)→F(c), so 
F
(
f
)
(
y
)
=
x
F(f)(y)=x is the condition.
### Cauchy (Karoubi) completion
**Given Definition:** The Cauchy completion of a category 
C
C is the universal category obtained by formally splitting all idempotents.
**Review:** Correct. It is also called the Karoubi envelope.
### Comma category
**Given Definition:** For functors 
F
:
A
→
C
F:A→C, 
G
:
B
→
C
G:B→C, the comma category 
(
F
↓
G
)
(F↓G) has objects triples 
(
a
,
b
,
f
)
(a,b,f) with 
f
:
F
(
a
)
→
G
(
b
)
f:F(a)→G(b), and morphisms 
(
g
,
h
)
(g,h) making the square commute.
**Review:** Correct.
### Composition (associativity, identity laws)
**Given Definition:** Associativity and identity laws as stated.
**Review:** Correct.
### Contravariant functor
**Given Definition:** A contravariant functor reverses composition: 
F
(
f
∘
g
)
=
F
(
g
)
∘
F
(
f
)
F(f∘g)=F(g)∘F(f).
**Review:** Correct. It is a covariant functor on the opposite category.
### Copower (tensoring with a set or object)
**Given Definition:** For a category 
C
C tensored over 
S
e
t
Set, the copower of 
X
X by a set 
S
S is an object 
S
⋅
X
S⋅X representing the functor 
C
(
X
,
−
)
S
C(X,−) 
S
 .
**Review:** Correct. The copower is the tensor with a set, and it is the colimit of the constant diagram at 
X
X indexed by 
S
S.
### Copresheaf
**Given Definition:** A copresheaf is a covariant functor 
F
:
C
→
S
e
t
F:C→Set.
**Review:** Correct. Though the term "copresheaf" is less common; it is often just called a covariant functor to Set.
### Coproduct
**Given Definition:** The coproduct of a family is an object with inclusions such that any cocone factors uniquely.
**Review:** Correct.
### Cosegment
**Given Definition:** A cosegment is an object 
I
I with two maps 
0
,
1
:
∗
⇉
I
0,1:∗⇉I (where 
∗
∗ is terminal) such that for any 
X
X, the map 
X
I
→
X
×
X
X 
I
 →X×X is a weak equivalence.
**Review:** This is non-standard. In a model category, a segment is an interval object for cylinder objects. The given definition seems to be for a path object. Typically, a segment (or interval) is used for cylinder objects, and a cosegment might be dual. However, the term "cosegment" is not common. The condition given is for a path object (which is a cosimplicial object in some contexts). This definition seems to be in a model categorical context, but it is not standard. It should be clarified that this is for a path object.
### Coslice category
**Given Definition:** For an object 
A
A in 
C
C, the coslice category 
A
/
C
A/C has objects morphisms 
f
:
A
→
X
f:A→X and morphisms 
h
:
X
→
Y
h:X→Y such that 
h
∘
f
=
g
h∘f=g.
**Review:** Correct. Also called the under category.
### Coequalizer
**Given Definition:** The coequalizer of 
f
,
g
:
X
⇉
Y
f,g:X⇉Y is 
q
:
Y
→
Z
q:Y→Z with 
q
∘
f
=
q
∘
g
q∘f=q∘g, universal.
**Review:** Correct.
### Coefficient
**Given Definition:** In enriched category theory or hyperdoctrines, a coefficient is an object in the base category.
**Review:** This is vague. In enriched category theory, the base category is often called the base of enrichment. In hyperdoctrines, coefficients might refer to objects over which we quantify. The definition is too brief and non-standard. It might be better to say that coefficients are objects in the base monoidal category or in the base for indexing.
### Coend
**Given Definition:** The coend of 
F
:
C
op
×
C
→
D
F:C 
op
 ×C→D is the coequalizer of the diagram with two arrows: one over morphisms and one over objects.
**Review:** Correct. The diagram is between the two morphisms that use the contravariance and covariance.
### Coreflective subcategory
**Given Definition:** A coreflective subcategory 
D
⊆
C
D⊆C is one for which the inclusion has a right adjoint (the coreflector).
**Review:** Correct.
### Covariant functor
**Given Definition:** A covariant functor preserves composition and identities.
**Review:** Correct.
### Dinatural transformation
**Given Definition:** A dinatural transformation 
α
:
F
⇒
¨
G
α:F 
⇒
¨
 G between functors 
F
,
G
:
C
op
×
C
→
D
F,G:C 
op
 ×C→D satisfies a coherence condition.
**Review:** The definition is incomplete. A dinatural transformation from 
F
F to 
G
G assigns to each object 
c
c a morphism 
α
c
:
F
(
c
,
c
)
→
G
(
c
,
c
)
α 
c
​
 :F(c,c)→G(c,c) such that for every 
f
:
c
→
c
′
f:c→c 
′
 , the hexagon commutes: 
G
(
f
,
id
c
′
)
∘
α
c
′
∘
F
(
id
c
,
f
)
=
G
(
id
c
,
f
)
∘
α
c
∘
F
(
f
,
id
c
′
)
G(f,id 
c 
′
 
​
 )∘α 
c 
′
 
​
 ∘F(id 
c
​
 ,f)=G(id 
c
​
 ,f)∘α 
c
​
 ∘F(f,id 
c 
′
 
​
 )
The given definition only says "satisfies a coherence condition", which is too vague.
### Dual category (opposite category)
**Given Definition:** The opposite category 
C
op
C 
op
  has the same objects and reversed morphisms.
**Review:** Correct.
### End
**Given Definition:** The end of 
F
:
C
op
×
C
→
D
F:C 
op
 ×C→D is the equalizer of a certain diagram.
**Review:** Correct.
### Equalizer
**Given Definition:** The equalizer of 
f
,
g
:
X
⇉
Y
f,g:X⇉Y is 
e
:
E
→
X
e:E→X with 
f
∘
e
=
g
∘
e
f∘e=g∘e, universal.
**Review:** Correct.
### Essentially surjective functor
**Given Definition:** A functor 
F
:
C
→
D
F:C→D is essentially surjective if for every 
D
D in 
D
D, there exists 
C
C in 
C
C with 
F
(
C
)
≅
D
F(C)≅D.
**Review:** Correct.
### Exact category
**Given Definition:** An exact category is an additive category with a distinguished class of short exact sequences (conflations) satisfying axioms.
**Review:** Correct. The axioms are those of Quillen exact categories.
### Factorization system (Epi–Mono, etc.)
**Given Definition:** A factorization system 
(
E
,
M
)
(E,M) consists of two classes of morphisms such that every morphism factors as an 
E
E-map followed by an 
M
M-map, and they are orthogonal.
**Review:** Correct. Orthogonality means that for every 
e
∈
E
e∈E and 
m
∈
M
m∈M, the commutative square has a unique diagonal filler.
### Fully faithful functor
**Given Definition:** A fully faithful functor induces bijections on hom-sets.
**Review:** Correct.
### Functor (covariant, contravariant)
**Given Definition:** Functors preserve composition and identities; contravariant reverses composition.
**Review:** Correct.
### Functor category
**Given Definition:** The functor category 
[
C
,
D
]
[C,D] has functors as objects and natural transformations as morphisms.
**Review:** Correct.
### Full functor
**Given Definition:** A full functor induces surjections on hom-sets.
**Review:** Correct.
### Grothendieck fibration
**Given Definition:** A Grothendieck fibration 
p
:
E
→
B
p:E→B is a functor such that for every morphism 
f
:
b
→
p
(
e
)
f:b→p(e) in 
B
B, there exists a Cartesian lift.
**Review:** Correct.
### Grothendieck topology
**Given Definition:** A Grothendieck topology on 
C
C is a collection of sieves (covering families) satisfying axioms.
**Review:** Correct.
### Image (regular image, categorical image)
**Given Definition:** The image of a morphism is the smallest subobject through which it factors.
**Review:** Correct in a category with subobjects. In abelian categories, it is the kernel of the cokernel.
### Initial object
**Given Definition:** An initial object has a unique morphism to every object.
**Review:** Correct.
### Isomorphism
**Given Definition:** An isomorphism has an inverse.
**Review:** Correct.
### Kan extension (left and right)
**Given Definition:** Given 
F
:
C
→
D
F:C→D, 
K
:
C
→
E
K:C→E, the right Kan extension 
Ran
K
F
Ran 
K
​
 F is the best approximation of 
F
F along 
K
K via a universal cone.
**Review:** Correct. The left Kan extension is similar but with a universal cocone.
### Kernel
**Given Definition:** In a category with zero morphisms, the kernel of 
f
:
X
→
Y
f:X→Y is the equalizer of 
f
f and the zero morphism.
**Review:** Correct.
### Lawvere theory
**Given Definition:** A Lawvere theory is a category 
T
T with finite products, objects are natural numbers, and 
n
n is the 
n
n-fold product of 
1
1. Models are finite product preserving functors.
**Review:** Correct.
### Limit (inverse limit, pullback, etc.)
**Given Definition:** A limit is a universal cone.
**Review:** Correct.
### Locally presentable category
**Given Definition:** A locally presentable category is cocomplete with a small set of small presentable generators.
**Review:** This is a bit imprecise. A locally presentable category is a cocomplete category that is locally presentable, meaning it has a small set of presentable objects and is accessible. The standard definition is: a category that is accessible and cocomplete.
### Monomorphism
**Given Definition:** A monomorphism is left-cancellative.
**Review:** Correct.
### Multicategory
**Given Definition:** A multicategory allows morphisms with multiple inputs.
**Review:** Correct.
### Natural transformation (vertical/horizontal composition)
**Given Definition:** A natural transformation assigns to each object a morphism such that naturality squares commute. Vertical composition is componentwise, horizontal composition is across functors.
**Review:** Correct.
### Natural isomorphism
**Given Definition:** A natural isomorphism is a natural transformation with invertible components.
**Review:** Correct.
### Nerve of a category
**Given Definition:** The nerve 
N
(
C
)
N(C) is a simplicial set with 
n
n-simplices as chains of 
n
n composable morphisms.
**Review:** Correct.
### Opposite category
**Given Definition:** Same as dual category.
**Review:** Correct.
### Power (exponentials, internal homs)
**Given Definition:** In a closed monoidal category, the power of 
X
X by 
S
S is 
X
S
X 
S
  representing 
C
(
S
⋅
(
−
)
,
X
)
C(S⋅(−),X).
**Review:** This is for tensoring with sets. In a closed category, the power by a set is the product of copies. The definition is correct for categories tensored over Set.
### Preadditive category
**Given Definition:** A preadditive category is enriched over Ab.
**Review:** Correct.
### Product
**Given Definition:** The product has projections and is universal.
**Review:** Correct.
### Pullback
**Given Definition:** The pullback of 
f
:
X
→
Z
f:X→Z, 
g
:
Y
→
Z
g:Y→Z is the limit of the cospan.
**Review:** Correct.
### Pushout
**Given Definition:** The pushout of 
f
:
Z
→
X
f:Z→X, 
g
:
Z
→
Y
g:Z→Y is the colimit of the span.
**Review:** Correct.
### Reflective subcategory
**Given Definition:** A reflective subcategory has a left adjoint to the inclusion.
**Review:** Correct.
### Representable functor
**Given Definition:** A representable functor is isomorphic to 
C
(
A
,
−
)
C(A,−) for some 
A
A.
**Review:** Correct.
### Retract (section/retraction)
**Given Definition:** An object 
A
A is a retract of 
B
B if there are 
s
:
A
→
B
s:A→B and 
r
:
B
→
A
r:B→A with 
r
∘
s
=
id
A
r∘s=id 
A
​
 .
**Review:** Correct.
### Slice category
**Given Definition:** For an object 
A
A, the slice category 
C
/
A
C/A has objects morphisms to 
A
A.
**Review:** Correct.
### Split exact sequence
**Given Definition:** A split exact sequence is a short exact sequence with a section.
**Review:** Correct.
### Split monomorphism / split epimorphism
**Given Definition:** A split monomorphism has a retraction; a split epimorphism has a section.
**Review:** Correct.
### Subobject (subobject classifier in a topos)
**Given Definition:** A subobject is an equivalence class of monomorphisms. In a topos, a subobject classifier 
Ω
Ω classifies subobjects.
**Review:** Correct.
### Terminal object
**Given Definition:** A terminal object has a unique morphism from every object.
**Review:** Correct.
### Universal arrow / universal property
**Given Definition:** A universal arrow from 
X
X to 
F
F is a pair 
(
A
,
u
:
X
→
F
(
A
)
)
(A,u:X→F(A)) that is initial.
**Review:** Correct.
### Weak limit / weak colimit
**Given Definition:** A weak limit is like a limit but without uniqueness of the mediating morphism.
**Review:** Correct.
### Zero object
**Given Definition:** A zero object is both initial and terminal.
**Review:** Correct.
### Zero morphism
**Given Definition:** In a category with a zero object, the zero morphism is the composite through the zero object.
**Review:** Correct.
Now, we move to higher category theory.
### Complicial set
**Given Definition:** A complicial set is a simplicial set with a marking (distinguished simplices) modeling 
(
∞
,
n
)
(∞,n)-categories.
**Review:** Correct, but the marking is for thin simplices or equivalences.
### Cellular set
**Given Definition:** A cellular set is a presheaf on 
Θ
n
Θ 
n
​
  (or 
Θ
Θ).
**Review:** Correct. 
Θ
n
Θ 
n
​
  is Joyal's cell category.
### Homotopy category
**Given Definition:** The homotopy category is obtained by formally inverting weak equivalences.
**Review:** Correct.
### n-category
**Given Definition:** An n-category has k-morphisms for 
k
≤
n
k≤n, with identities for 
k
>
n
k>n.
**Review:** This is for strict n-categories. For weak n-categories, higher morphisms are not necessarily identities but are invertible above dimension n.
### ∞-category
**Given Definition:** An ∞-category has k-morphisms for all k, invertible for 
k
≥
2
k≥2, with composition associative up to higher morphisms.
**Review:** This is for 
(
∞
,
1
)
(∞,1)-categories. The term ∞-category often means 
(
∞
,
1
)
(∞,1)-category.
### Weak n-category
**Given Definition:** A weak n-category has composition associative and unital up to coherent higher isomorphisms.
**Review:** Correct.
### Strict n-category
**Given Definition:** A strict n-category is a category enriched over strict (n-1)-categories.
**Review:** Correct.
### Bicategory
**Given Definition:** A bicategory has 1-morphisms composing associatively up to isomorphism, and 2-morphisms.
**Review:** Correct.
### Globular set
**Given Definition:** A globular set is a presheaf on the globe category, with source and target maps.
**Review:** Correct.
### Nerve of a category
**Review:** Already covered.
### Quasicategory
**Given Definition:** A quasicategory is a simplicial set satisfying the inner horn filling condition.
**Review:** Correct.
### Kan complex
**Given Definition:** A Kan complex is a simplicial set where every horn has a filler.
**Review:** Correct.
### Simplicial set
**Given Definition:** A simplicial set is a presheaf on the simplex category.
**Review:** Correct.
### Complete Segal space
**Given Definition:** A complete Segal space is a simplicial space satisfying Segal conditions and completeness.
**Review:** Correct.
### Segal category
**Given Definition:** A Segal category is a simplicial space with discrete 
X
0
X 
0
​
  and Segal maps weak equivalences.
**Review:** Correct.
### Homotopy hypothesis
**Given Definition:** The homotopy hypothesis states that homotopy types are equivalent to ∞-groupoids.
**Review:** Correct.
### Cartesian closed category
**Given Definition:** A Cartesian closed category has finite products and internal homs.
**Review:** Correct.
### Closed category
**Given Definition:** A closed category has internal homs and a unit object.
**Review:** Correct, though the definition might vary. Eilenberg-Kelly defined it with extra structure.
### Compact closed category
**Given Definition:** A compact closed category is a symmetric monoidal category where every object has a dual.
**Review:** Correct.
### Double category
**Given Definition:** A double category has horizontal and vertical morphisms and squares.
**Review:** Correct.
### Enriched category
**Given Definition:** An enriched category over 
V
V has hom-objects in 
V
V, with composition and identities.
**Review:** Correct.
### Internal category
**Given Definition:** An internal category in 
E
E has objects and morphisms in 
E
E, with source, target, identity, composition.
**Review:** Correct.
### Monoidal category
**Given Definition:** A monoidal category has a tensor product, unit, associator, unitors, with coherence.
**Review:** Correct.
### Braided monoidal category
**Given Definition:** A braided monoidal category has a braiding satisfying hexagons.
**Review:** Correct.
### Monoidal ∞-category
**Given Definition:** A monoidal ∞-category has a coherent tensor product.
**Review:** Correct.
### Omega-category (ω-category)
**Given Definition:** An ω-category is a strict ∞-category.
**Review:** Correct.
### Pivotal category
**Given Definition:** A pivotal category is a rigid monoidal category with a self-duality isomorphism.
**Review:** Correct.
### Fusion category
**Given Definition:** A fusion category is a semisimple rigid monoidal category with finitely many simples, finite-dimensional hom-spaces, and simple unit.
**Review:** Correct.
### Modular tensor category
**Given Definition:** A modular tensor category is a ribbon fusion category with non-degenerate S-matrix.
**Review:** Correct.
### Symmetric monoidal category
**Given Definition:** A symmetric monoidal category is braided with symmetric braiding.
**Review:** Correct.
### k-morphism
**Given Definition:** In an n-category, a k-morphism is a morphism at level k.
**Review:** Correct.
### 2-morphism
**Given Definition:** A 2-morphism is a morphism between 1-morphisms.
**Review:** Correct.
### Higher morphism
**Given Definition:** A higher morphism is a k-morphism for k≥2.
**Review:** Correct.
### Globular k-cell
**Given Definition:** A globular k-cell is a k-morphism in a globular set.
**Review:** Correct.
### Icon
**Given Definition:** An icon is a 2-cell between lax functors that is trivial on objects.
**Review:** Correct.
### Lax natural transformation
**Given Definition:** A lax natural transformation has 2-cells for each 1-cell, not necessarily invertible.
**Review:** Correct.
### Oplax natural transformation
**Given Definition:** Like lax but with reversed 2-cells.
**Review:** Correct.
### Pseudonatural transformation
**Given Definition:** A pseudonatural transformation has invertible 2-cells.
**Review:** Correct.
### Modification
**Given Definition:** A modification is a 3-cell between pseudonatural transformations.
**Review:** Correct.
### Equivalence in higher categories
**Given Definition:** An equivalence has an inverse and invertible 2-cells.
**Review:** Correct for 1-morphisms in a higher category.
### Adjoint equivalence
**Given Definition:** An adjoint equivalence is an equivalence that is also an adjunction with invertible unit and counit.
**Review:** Correct.
### ∞-functor
**Given Definition:** An ∞-functor between ∞-categories preserves composition up to higher morphisms.
**Review:** Correct.
### Functor between bicategories
**Given Definition:** A functor between bicategories consists of mappings on objects and morphisms, with coherence isomorphisms.
**Review:** Correct.
### Homotopy coherent diagram
**Given Definition:** A homotopy coherent diagram is a simplicial functor from the simplicial category of the nerve.
**Review:** Correct.
### Lax functor
**Given Definition:** A lax functor has coherence morphisms that are not necessarily invertible.
**Review:** Correct.
### Oplax functor
**Given Definition:** Similar to lax but with reversed coherence morphisms.
**Review:** Correct.
### Pseudofunctor
**Given Definition:** A pseudofunctor has invertible coherence morphisms.
**Review:** Correct.
### Transformation between ∞-functors
**Given Definition:** A transformation is a morphism in the functor ∞-category.
**Review:** Correct.
### Natural isomorphism up to higher equivalence
**Given Definition:** A natural isomorphism up to higher equivalence has each component an equivalence.
**Review:** Correct.
### Homotopy colimit
**Given Definition:** The homotopy colimit is the derived functor of the colimit.
**Review:** Correct in a model category.
### Homotopy limit
**Given Definition:** The homotopy limit is the derived functor of the limit.
**Review:** Correct.
### ∞-categorical colimit
**Given Definition:** The ∞-categorical colimit is a universal cocone defined via Kan extension.
**Review:** Correct.
### ∞-categorical limit
**Given Definition:** The ∞-categorical limit is a universal cone defined via Kan extension.
**Review:** Correct.
### Weighted limit
**Given Definition:** A weighted limit is defined by a weight functor in enriched category theory.
**Review:** Correct.
### Bicolimit
**Given Definition:** A bicolimit is a colimit defined up to equivalence in a bicategory.
**Review:** Correct.
### Flexible limit
**Given Definition:** A flexible limit is a 2-dimensional limit preserved by all 2-functors.
**Review:** This is not standard. Flexible limits are a class of 2-dimensional limits that are cofibrant replacements of strict limits. The given definition is vague.
### Kan extension in higher categories
**Given Definition:** Kan extension in ∞-categories is the best approximation along a functor.
**Review:** Correct.
### Lax limit
**Given Definition:** A lax limit has a universal cone commuting up to non-invertible 2-cells.
**Review:** Correct.
### Pseudolimit
**Given Definition:** A pseudolimit has a universal cone commuting up to invertible 2-cells.
**Review:** Correct.
### End (as a limiting construction)
**Review:** Already covered.
### Bilimit
**Given Definition:** A bilimit is a 2-dimensional limit defined up to equivalence.
**Review:** Correct.
### Adjunction in bicategories
**Given Definition:** An adjunction in a bicategory has unit and counit satisfying triangle identities up to invertible 3-cells.
**Review:** Correct.
### Biadjunction
**Given Definition:** A biadjunction is an adjunction in a bicategory with pseudonatural unit and counit.
**Review:** Correct.
### Lax adjunction
**Given Definition:** A lax adjunction has unit and counit that are not necessarily invertible.
**Review:** Correct.
### ∞-adjunction
**Given Definition:** An ∞-adjunction has unit and counit satisfying triangle identities up to higher equivalence.
**Review:** Correct.
### Coend calculus
**Given Definition:** Coend calculus uses coends to express constructions.
**Review:** Correct, but it's a technique, not a definition.
### Dualizable object
**Given Definition:** A dualizable object has a dual with unit and counit satisfying zigzags.
**Review:** Correct.
### Fully dualizable object
**Given Definition:** In a symmetric monoidal (∞,n)-category, a fully dualizable object has duals at all levels.
**Review:** Correct.
### Serre duality
**Given Definition:** Serre duality is a duality for sheaf cohomology on smooth projective varieties.
**Review:** Correct.
### Verdier duality
**Given Definition:** Verdier duality is a duality for sheaves on locally compact spaces.
**Review:** Correct.
### Grothendieck duality
**Given Definition:** Grothendieck duality extends Serre duality to relative settings.
**Review:** Correct.
### Monad in a bicategory
**Given Definition:** A monad in a bicategory is a 1-cell with multiplication and unit.
**Review:** Correct.
### Comonad
**Given Definition:** A comonad is the dual of a monad.
**Review:** Correct.
### Eilenberg–Moore object
**Given Definition:** The Eilenberg-Moore object of a monad is the universal object for algebras.
**Review:** Correct.
### Kleisli object
**Given Definition:** The Kleisli object is the universal object for free algebras.
**Review:** Correct.
### Distributive law
**Given Definition:** A distributive law between monads is a natural transformation 
S
T
⇒
T
S
ST⇒TS making 
T
S
TS a monad.
**Review:** Correct.
### Algebras for a monad
**Given Definition:** An algebra for a monad is an object with an action satisfying axioms.
**Review:** Correct.
### Coalgebras
**Given Definition:** Coalgebras are dual to algebras.
**Review:** Correct.
### Monadic functor
**Given Definition:** A monadic functor is equivalent to the forgetful functor from algebras.
**Review:** Correct.
### Barr–Beck theorem
**Given Definition:** The Barr-Beck theorem gives conditions for a functor to be monadic.
**Review:** Correct.
### Lax algebra
**Given Definition:** A lax algebra over a monad has a lax action.
**Review:** Correct.
### Pseudo-monad
**Given Definition:** A pseudo-monad has coherence isomorphisms.
**Review:** Correct.
### Pseudo-algebra
**Given Definition:** A pseudo-algebra has coherence isomorphisms for the action.
**Review:** Correct.
### Operad
**Given Definition:** An operad has operations with symmetric group actions and composition.
**Review:** Correct.
### Multicategory
**Given Definition:** A multicategory has morphisms with multiple inputs.
**Review:** Correct.
### PROP
**Given Definition:** A PROP is a symmetric monoidal category with objects natural numbers and tensor product addition.
**Review:** Correct.
### Lawvere theory
**Review:** Already covered.
### Topological operad
**Given Definition:** A topological operad is an operad in topological spaces.
**Review:** Correct.
### Symmetric operad
**Given Definition:** A symmetric operad has symmetric group actions.
**Review:** Correct.
### Cyclic operad
**Given Definition:** A cyclic operad has cyclic actions on operations.
**Review:** Correct.
### Modular operad
**Given Definition:** A modular operad allows compositions along graphs with genus.
**Review:** Correct.
### Algebra over an operad
**Given Definition:** An algebra over an operad is an object with action maps.
**Review:** Correct.
### Coalgebra over an operad
**Given Definition:** A coalgebra over an operad has coaction maps.
**Review:** Correct.
### ∞-operad
**Given Definition:** An ∞-operad is an ∞-categorical operad.
**Review:** Correct.
### Dendroidal set
**Given Definition:** A dendroidal set is a presheaf on the tree category.
**Review:** Correct.
### Colored operad
**Given Definition:** A colored operad has operations with specified input and output colors.
**Review:** Correct.
### Properad
**Given Definition:** A properad allows operations with multiple inputs and outputs, composed along graphs.
**Review:** Correct.
### ∞-properad
**Given Definition:** An ∞-properad is a properad in higher category theory.
**Review:** Correct.
### Classifying space
**Given Definition:** The classifying space 
B
G
BG satisfies 
Ω
B
G
≃
G
ΩBG≃G.
**Review:** Correct for a group.
### Delooping
**Given Definition:** Delooping constructs 
B
G
BG from 
G
G.
**Review:** Correct.
### Loop space
**Given Definition:** The loop space 
Ω
X
ΩX is the space of based loops.
**Review:** Correct.
### Loop space object
**Given Definition:** In an (∞,1)-category, the loop space object is the pullback of 
∗
→
X
←
∗
∗→X←∗.
**Review:** Correct.
### Mapping space
**Given Definition:** The mapping space in an (∞,1)-category is the ∞-groupoid of morphisms.
**Review:** Correct.
### Fundamental ∞-groupoid
**Given Definition:** The fundamental ∞-groupoid of a space is its ∞-groupoid of paths.
**Review:** Correct.
### Homotopy fiber
**Given Definition:** The homotopy fiber is the pullback of a point inclusion.
**Review:** Correct.
### Homotopy n-type
**Given Definition:** A homotopy n-type has trivial homotopy groups above dimension n.
**Review:** Correct.
### Homotopy quotient
**Given Definition:** The homotopy quotient is the Borel construction.
**Review:** Correct.
### Stabilization
**Given Definition:** Stabilization is the process of forming spectrum objects.
**Review:** Correct.
### Suspension
**Given Definition:** Suspension is the left adjoint to the loop space functor.
**Review:** Correct.
### 2-category
**Given Definition:** A 2-category is a category enriched over Cat.
**Review:** Correct.
### 3-category
**Given Definition:** A 3-category is enriched over 2-categories.
**Review:** Correct.
### n-fold category
**Given Definition:** An n-fold category is internal to (n-1)-fold categories.
**Review:** Correct.
### Iterated span category
**Given Definition:** An iterated span category is built by iteratively taking spans.
**Review:** Correct.
### Gray-category
**Given Definition:** A Gray-category is a semi-strict 3-category.
**Review:** Correct.
### Trimble n-category
**Given Definition:** A Trimble n-category is defined using operads and topological enrichment.
**Review:** Correct.
### Tamsamani n-category
**Given Definition:** A Tamsamani n-category is defined using simplicial objects.
**Review:** Correct.
### Street nerve
**Given Definition:** The Street nerve is for strict ω-categories.
**Review:** Correct.
### Θ-space
**Given Definition:** A Θ-space is a presheaf on 
Θ
n
Θ 
n
​
  modeling (∞,n)-categories.
**Review:** Correct.
### Rezk completion
**Given Definition:** The Rezk completion is a fibrant replacement for Segal spaces.
**Review:** Correct.
### Homotopy coherent nerve
**Given Definition:** The homotopy coherent nerve of a simplicial category is a simplicial set.
**Review:** Correct.
### ω-category
**Review:** Already covered.
### Derived stack
**Given Definition:** A derived stack is a stack in derived algebraic geometry.
**Review:** Correct.
### Higher stack
**Given Definition:** A higher stack takes values in ∞-groupoids.
**Review:** Correct.
### Perfect stack
**Given Definition:** A perfect stack has category of quasi-coherent sheaves generated by perfect complexes.
**Review:** Correct.
### Geometric Langlands program
**Given Definition:** The geometric Langlands program relates D-modules to local systems.
**Review:** Correct.
### Topological field theory
**Given Definition:** A TFT is a symmetric monoidal functor from bordisms to vector spaces.
**Review:** Correct.
### Extended TQFT
**Given Definition:** An extended TQFT is a functor from higher bordisms to higher vector spaces.
**Review:** Correct.
### Conformal field theory
**Given Definition:** A CFT is a quantum field theory invariant under conformal transformations.
**Review:** Correct.
### Factorization algebra
**Given Definition:** A factorization algebra assigns algebras to opens with multiplication for disjoint unions.
**Review:** Correct.
### Chiral algebra
**Given Definition:** A chiral algebra is a Lie algebra in D-modules with a chiral bracket.
**Review:** Correct.
### Vertex operator algebra
**Given Definition:** A VOA has state-field correspondence and operator product expansion.
**Review:** Correct.
### Deformation quantization
**Given Definition:** Deformation quantization deforms commutative algebras to star-products.
**Review:** Correct.
### Drinfeld center
**Given Definition:** The Drinfeld center is the braided category of half-braidings.
**Review:** Correct.
### Hochschild cohomology
**Given Definition:** Hochschild cohomology classifies deformations.
**Review:** Correct.
### Cyclic homology
**Given Definition:** Cyclic homology incorporates a circle action.
**Review:** Correct.
### A∞-algebra
**Given Definition:** An A∞-algebra has higher operations satisfying Stasheff identities.
**Review:** Correct.
### A∞-category
**Given Definition:** An A∞-category has higher compositions.
**Review:** Correct.
### L∞-algebra
**Given Definition:** An L∞-algebra has higher brackets with Jacobi identities up to homotopy.
**Review:** Correct.
### dg-category
**Given Definition:** A dg-category is enriched over chain complexes.
**Review:** Correct.
### Spectral category
**Given Definition:** A spectral category is enriched over spectra.
**Review:** Correct.
### Shifted symplectic structure
**Given Definition:** A shifted symplectic structure is a closed 2-form of degree k that is non-degenerate.
**Review:** Correct.
### Factorization homology
**Given Definition:** Factorization homology integrates an E_n-algebra over a framed n-manifold.
**Review:** Correct.
## Summary of Corrections
Most definitions are accurate. The following needed attention:
1. **Cosegment**: The definition is non-standard and seems to describe a path object in a model category. It should be clarified or labeled as non-standard.
2. **Coefficient**: The definition is too vague. It should specify that in enriched category theory, it's an object of the base monoidal category, and in hyperdoctrines, it might be an object for indexing.
3. **Dinatural transformation**: The definition is incomplete; it should include the hexagon condition.
4. **Flexible limit**: The definition is vague and not standard; it should refer to a class of 2-limits that are cofibrant.
Overall, the list is very comprehensive and mostly accurate.