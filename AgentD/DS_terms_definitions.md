### Classical Category Theory

* **Abelian category**: An additive category with finite limits and colimits, where every monomorphism is a kernel and every epimorphism is a cokernel, and all epi-mono factorizations exist.
* **Additive category**: A preadditive category with finite biproducts.
* **Adjoint functor theorem**: Conditions (e.g., preservation of limits) guaranteeing a functor has a left/right adjoint (e.g., Freyd's GAFT).
* **Adjunction**: A pair of functors \(F: \mathcal{C} \rightleftarrows \mathcal{D} :G\) with natural transformations \(\eta: 1_{\mathcal{C}} \to GF\) (unit) and \(\varepsilon: FG \to 1_{\mathcal{D}}\) (counit) satisfying triangle identities.
* **Automorphism**: An invertible endomorphism (isomorphism from an object to itself).
* **Balanced category**: A category where every bimorphism (monic and epic morphism) is an isomorphism.
* **Category**: A collection of objects and morphisms with associative composition and identity morphisms. **Small**: Objects and morphisms form a set. **Large**: Objects/morphisms form a proper class. **Locally small**: Hom-sets are sets.
* **Category of elements**: For \(F: \mathcal{C}^{\text{op}} \to \mathbf{Set}\), the category \(\int F\) with objects \((c, x)\) where \(c \in \mathcal{C}\), \(x \in F(c)\), and morphisms \((c, x) \to (c', x')\) are \(f: c \to c'\) with \(F(f)(x') = x\).
* **Cauchy (Karoubi) completion**: The smallest category containing all idempotent splittings of a given category.
* **Comma category**: For functors \(F: \mathcal{A} \to \mathcal{C}\), \(G: \mathcal{B} \to \mathcal{C}\), the category \((F \downarrow G)\) with objects \((A, B, f)\) where \(A \in \mathcal{A}\), \(B \in \mathcal{B}\), \(f: FA \to GB\), and morphisms \((A, B, f) \to (A', B', f')\) are pairs \((a: A \to A', b: B \to B')\) with \(f' \circ Fa = Gb \circ f\).
* **Composition**: A partial binary operation \(\circ\) on morphisms satisfying associativity and identity laws: \(f \circ (g \circ h) = (f \circ g) \circ h\) and \(1_B \circ f = f = f \circ 1_A\) for \(f: A \to B\).
* **Contravariant functor**: A functor \(F: \mathcal{C}^{\text{op}} \to \mathcal{D}\) reversing morphism directions.
* **Copower**: For object \(C\) and set \(I\), the coproduct \(\coprod_{i \in I} C\) (tensoring with a discrete category).
* **Copresheaf**: A functor \(\mathcal{C} \to \mathbf{Set}\) (covariant presheaf).
* **Coproduct**: The colimit of a discrete diagram; universal cocone over two objects.
* **Cosegment**: A morphism from an initial object (dual to segment).
* **Coslice category**: For object \(c \in \mathcal{C}\), the category \(c \downarrow \mathcal{C}\) with objects \((f, d)\) where \(f: c \to d\), and morphisms commuting with \(f\).
* **Coequalizer**: The colimit of a parallel pair \(f, g: A \to B\); universal morphism \(q: B \to Q\) with \(qf = qg\).
* **Coefficient**: In enriched contexts, objects in the base monoidal category \(\mathcal{V}\); in hyperdoctrines, objects quantifying over terms.
* **Coend**: For \(T: \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}\), the coend \(\int^c T(c, c)\) is the coequalizer of \(\coprod_{f: c \to c'} T(c', c) \rightrightarrows \coprod_{c} T(c, c)\).
* **Coreflective subcategory**: A subcategory \(\mathcal{A} \subseteq \mathcal{C}\) where the inclusion has a right adjoint.
* **Covariant functor**: A functor \(F: \mathcal{C} \to \mathcal{D}\) preserving morphism directions.
* **Dinatural transformation**: For \(S, T: \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}\), a family \(\alpha_c: S(c, c) \to T(c, c)\) such that for \(f: c \to c'\), \(T(1, f) \circ \alpha_c \circ S(f, 1) = T(f, 1) \circ \alpha_{c'} \circ S(1, f)\).
* **Dual category (opposite category)**: \(\mathcal{C}^{\text{op}}\) with objects same as \(\mathcal{C}\) and morphisms reversed.
* **End**: For \(T: \mathcal{C}^{\text{op}} \times \mathcal{C} \to \mathcal{D}\), the end \(\int_c T(c, c)\) is the equalizer of \(\prod_c T(c, c) \rightrightarrows \prod_{f: c \to c'} T(c, c')\).
* **Equalizer**: The limit of a parallel pair \(f, g: A \to B\); universal morphism \(e: E \to A\) with \(fe = ge\).
* **Essentially surjective functor**: A functor \(F: \mathcal{C} \to \mathcal{D}\) where every \(d \in \mathcal{D}\) is isomorphic to \(F(c)\) for some \(c \in \mathcal{C}\).
* **Exact category**: An additive category with exact sequences satisfying the Eilenberg–Moore axioms.
* **Factorization system**: A pair \((\mathcal{E}, \mathcal{M})\) of morphism classes where every morphism factors as \(\mathcal{E}\)-morphism followed by \(\mathcal{M}\)-morphism, with unique diagonal fill-ins.
* **Fully faithful functor**: A functor \(F\) inducing bijections \(\text{Hom}_{\mathcal{C}}(c, c') \cong \text{Hom}_{\mathcal{D}}(Fc, Fc')\).
* **Functor**: A morphism-preserving map between categories. **Covariant**: \(F: \mathcal{C} \to \mathcal{D}\). **Contravariant**: \(F: \mathcal{C}^{\text{op}} \to \mathcal{D}\).
* **Functor category**: For small \(\mathcal{C}, \mathcal{D}\), the category \([\mathcal{C}, \mathcal{D}]\) with functors as objects and natural transformations as morphisms.
* **Full functor**: A functor \(F\) inducing surjections \(\text{Hom}_{\mathcal{C}}(c, c') \to \text{Hom}_{\mathcal{D}}(Fc, Fc')\).
* **Grothendieck fibration**: A functor \(P: \mathcal{E} \to \mathcal{B}\) where morphisms in \(\mathcal{E}\) lift "cartesianly" over morphisms in \(\mathcal{B}\).
* **Grothendieck topology**: On a category \(\mathcal{C}\), an assignment to each object \(c\) of covering sieves satisfying stability and transitivity axioms.
* **Image**: For \(f: A \to B\), the smallest subobject of \(B\) through which \(f\) factors. **Regular image**: The image in a regular category.
* **Initial object**: An object \(I\) with exactly one morphism to every object.
* **Isomorphism**: A morphism \(f: A \to B\) with inverse \(g: B \to A\) such that \(fg = 1_B\) and \(gf = 1_A\).
* **Kan extension**: For \(F: \mathcal{C} \to \mathcal{E}\), \(K: \mathcal{C} \to \mathcal{D}\), the **left Kan extension** \(\text{Lan}_K F\) satisfies \(\text{Hom}(\text{Lan}_K F, G) \cong \text{Hom}(F, G \circ K)\). **Right Kan extension** dual.
* **Kernel**: For \(f: A \to B\) in a pointed category, the equalizer of \(f\) and \(0\).
* **Lawvere theory**: A category \(\mathcal{L}\) with finite products and a distinguished object \(X\) such that every object is \(X^n\).
* **Limit**: The universal cone over a diagram; e.g., **inverse limit** for diagrams in posets, **pullback** for cospans.
* **Locally presentable category**: A cocomplete category with a strong generator of presentable objects.
* **Monomorphism**: A morphism \(f: A \to B\) such that \(fg = fh\) implies \(g = h\).
* **Multicategory**: A generalization of categories where morphisms have finite lists of inputs and one output.
* **Natural transformation**: For functors \(F, G: \mathcal{C} \to \mathcal{D}\), a family \(\eta_c: Fc \to Gc\) with \(\eta_{c'} \circ Ff = Gf \circ \eta_c\) for \(f: c \to c'\). **Vertical composition**: \((\eta \circ \epsilon)_c = \eta_c \circ \epsilon_c\). **Horizontal composition**: \((\eta \bullet \epsilon)_c = G\eta_c \circ \epsilon_{Fc} = \epsilon_{Gc} \circ F\eta_c\).
* **Natural isomorphism**: A natural transformation where each \(\eta_c\) is an isomorphism.
* **Nerve of a category**: The simplicial set \(N(\mathcal{C})\) with \(n\)-simplices as sequences of composable morphisms \(c_0 \to c_1 \to \cdots \to c_n\).
* **Opposite category**: \(\mathcal{C}^{\text{op}}\) with objects same as \(\mathcal{C}\) and morphisms reversed.
* **Power**: For object \(C\) and set \(I\), the product \(\prod_{i \in I} C\) (cotensoring in enriched contexts).
* **Preadditive category**: A category enriched over abelian groups.
* **Product**: The limit of a discrete diagram; universal cone over two objects.
* **Pullback**: The limit of a cospan \(A \to C \leftarrow B\); universal square commuting with the cospan.
* **Pushout**: The colimit of a span \(A \leftarrow C \to B\); universal square commuting with the span.
* **Reflective subcategory**: A subcategory \(\mathcal{A} \subseteq \mathcal{C}\) where the inclusion has a left adjoint.
* **Representable functor**: A functor isomorphic to \(\text{Hom}_{\mathcal{C}}(c, -)\) for some object \(c\).
* **Retract**: \(A\) is a retract of \(B\) if there exist \(i: A \to B\) (section) and \(r: B \to A\) (retraction) with \(r \circ i = 1_A\).
* **Slice category**: For object \(c \in \mathcal{C}\), the category \(\mathcal{C} \downarrow c\) with objects \((f, d)\) where \(f: d \to c\), and morphisms commuting with \(f\).
* **Split exact sequence**: An exact sequence \(0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0\) with sections/splittings.
* **Split monomorphism / split epimorphism**: A monomorphism \(i\) with left inverse (\(r \circ i = 1\)), or epimorphism \(p\) with right inverse.
* **Subobject**: An equivalence class of monomorphisms into an object. **Subobject classifier**: In a topos, an object \(\Omega\) with natural bijection \(\text{Sub}(c) \cong \text{Hom}(c, \Omega)\).
* **Terminal object**: An object \(T\) with exactly one morphism from every object.
* **Universal arrow / universal property**: For \(U: \mathcal{D} \to \mathcal{C}\), a universal arrow from \(c\) to \(U\) is a pair \((d, \eta: c \to Ud)\) such that every \(f: c \to Ud'\) factors uniquely as \(Uf' \circ \eta\) for \(f': d \to d'\).
* **Weak limit / weak colimit**: A cone satisfying existence but not necessarily uniqueness in the universal property.
* **Zero object**: An object that is both initial and terminal.
* **Zero morphism**: The unique morphism \(A \to 0 \to B\) through a zero object.

---

### Basic Higher Category Concepts

* **Complicial set**: A simplicial set with marked thin simplices, modeling \((\infty, n)\)-categories.
* **Cellular set**: A presheaf on a category of cell complexes (e.g., for modeling higher categories).
* **Homotopy category**: For an \(\infty\)-category \(\mathcal{C}\), the category \(\text{h}\mathcal{C}\) with same objects and homotopy classes of 1-morphisms.
* **n-category**: A category with k-morphisms for \(k \leq n\) and composition coherent up to equivalence.
* **∞-category**: A category with k-morphisms for all \(k \in \mathbb{N}\), often modeled by simplicial sets (quasicategories).
* **Weak n-category**: An n-category where composition is associative and unital up to coherent equivalence.
* **Strict n-category**: An n-category where composition is strictly associative and unital (globular sets with strict laws).
* **Bicategory**: A weak 2-category with objects, 1-morphisms, 2-morphisms, and associative/unital composition up to coherent isomorphism.
* **Globular set**: A presheaf on the globe category \(\mathbb{G}\) (objects \(0,1,2,\ldots\), morphisms \(s,t: n \to n+1\)).
* **Nerve of a category**: As defined in classical category theory.
* **Quasicategory**: A simplicial set where every inner horn has a filler (weak Kan complex).
* **Kan complex**: A simplicial set where every horn has a filler.
* **Simplicial set**: A functor \(\mathbf{\Delta}^{\text{op}} \to \mathbf{Set}\).
* **Complete Segal space**: A simplicial space \(W: \mathbf{\Delta}^{\text{op}} \to \mathbf{sSet}\) that is Reedy fibrant, Segal (pullback condition), and complete (essentially constant on equivalences).
* **Segal category**: A simplicial space satisfying the Segal condition but not necessarily completeness.
* **Homotopy hypothesis**: The principle that \(\infty\)-groupoids model homotopy types, and n-groupoids model n-types.

---

### Types of Higher Categories

* **Cartesian closed category**: A category with finite products and exponentials (internal homs).
* **Closed category**: A category with internal hom-objects \(\underline{\text{Hom}}(A, B)\) and unit object.
* **Compact closed category**: A symmetric monoidal category where every object has a dual.
* **Double category**: A category with two types of morphisms (horizontal and vertical) and squares as 2-cells.
* **Enriched category**: A category where hom-sets are replaced by objects in a monoidal category \(\mathcal{V}\).
* **Internal category**: In a category \(\mathcal{E}\), a pair of objects \(C_0, C_1\) with source/target, identity, and composition morphisms satisfying category axioms.
* **Monoidal category**: A category \(\mathcal{C}\) with tensor product \(\otimes\), unit \(I\), and associator/unitor natural isomorphisms satisfying coherence.
* **Braided monoidal category**: A monoidal category with braiding \(\beta_{A,B}: A \otimes B \to B \otimes A\) satisfying hexagon axioms.
* **Monoidal ∞-category**: An \(\infty\)-category with a monoidal structure (coherently associative/unital tensor product).
* **Omega-category (ω-category)**: A strict \(\infty\)-category with globular composition and strict laws.
* **Pivotal category**: A monoidal category where every object has a dual and the duals are compatible with evaluation/coevaluation.
* **Fusion category**: A semisimple rigid monoidal category with finitely many simple objects and finite-dimensional hom-spaces.
* **Modular tensor category**: A braided fusion category with non-degenerate braiding.
* **Symmetric monoidal category**: A braided monoidal category with symmetric braiding (\(\beta_{B,A} \circ \beta_{A,B} = 1_{A \otimes B}\)).
* **Virtual double category**: A generalization of double categories with objects, vertical/horizontal morphisms, and cells, but without all compositions.

---

### Morphisms & Cells

* **k-morphism**: A morphism between (k-1)-morphisms in a higher category.
* **2-morphism**: A morphism between 1-morphisms (e.g., natural transformation in 2-categories).
* **Higher morphism**: General term for k-morphisms with \(k \geq 2\).
* **Globular k-cell**: A k-morphism in a globular set or strict higher category.
* **Icon**: An "Identity Component Oplax Natural transformation" between 2-functors.
* **Lax natural transformation**: For 2-functors \(F, G: \mathcal{C} \to \mathcal{D}\), a family \(\eta_c: Fc \to Gc\) with 2-cells \(\eta_f: Gf \circ \eta_c \Rightarrow \eta_{c'} \circ Ff\) satisfying coherence.
* **Oplax natural transformation**: As above but with 2-cells \(\eta_f: \eta_{c'} \circ Ff \Rightarrow Gf \circ \eta_c\).
* **Pseudonatural transformation**: A lax natural transformation where the 2-cells \(\eta_f\) are invertible.
* **Modification**: For pseudonatural transformations \(\eta, \mu: F \to G\), a family of 2-cells \(\Gamma_c: \eta_c \Rightarrow \mu_c\) commuting with \(\eta_f, \mu_f\).
* **Equivalence in higher categories**: A k-morphism that is invertible up to higher equivalence.
* **Adjoint equivalence**: An equivalence equipped with unit and counit satisfying higher triangle identities.

---

### Functors & Transformations

* **∞-functor**: A functor between \(\infty\)-categories (e.g., a simplicial map preserving inner horn fillers).
* **Functor between bicategories**: A pseudofunctor (preserves composition and identity up to coherent isomorphism).
* **Homotopy coherent diagram**: A diagram in an \(\infty\)-category encoding higher commutativity.
* **Lax functor**: A functor \(F: \mathcal{C} \to \mathcal{D}\) with morphisms \(Ff \circ Fg \to F(f \circ g)\) and \(1_{Fc} \to F(1_c)\), satisfying coherence.
* **Oplax functor**: As above but with 2-cells \(F(f \circ g) \to Ff \circ Fg\) and \(F(1_c) \to 1_{Fc}\).
* **Pseudofunctor**: A lax functor where the comparison 2-cells are invertible.
* **Transformation between ∞-functors**: A natural transformation in the \(\infty\)-categorical sense (e.g., a simplicial homotopy).
* **Natural isomorphism up to higher equivalence**: A natural transformation where components are equivalences, and coherence holds up to higher cells.

---

### Limits & Colimits

* **Homotopy colimit**: A colimit in a homotopy-invariant sense (e.g., in model categories or \(\infty\)-categories).
* **Homotopy limit**: A limit in a homotopy-invariant sense.
* **∞-categorical colimit**: A colimit in an \(\infty\)-category (universal cocone up to contractible choices).
* **∞-categorical limit**: A limit in an \(\infty\)-category (universal cone up to contractible choices).
* **Weighted limit**: A limit indexed by a functor and a weight (enriched context).
* **Bicolimit**: A bicategorical colimit satisfying a universal property up to equivalence.
* **Flexible limit**: A limit that is "homotopically well-behaved" (e.g., preserved by 2-functors with left adjoints).
* **Kan extension in higher categories**: The homotopy-invariant version of Kan extensions (e.g., in \(\infty\)-categories).
* **Lax limit**: A limit where cones commute up to non-invertible 2-cells.
* **Pseudolimit**: A limit where cones commute up to invertible 2-cells.
* **End (as a limiting construction)**: The invariant end in enriched higher categories.
* **Bilimit**: Synonym for bicolimit.

---

### Adjunctions & Duality

* **Adjunction in bicategories**: For objects \(C, D\), 1-morphisms \(f: C \to D\), \(g: D \to C\), and 2-cells \(\eta: 1_C \to g \circ f\), \(\varepsilon: f \circ g \to 1_D\) satisfying triangle identities.
* **Biadjunction**: An adjunction in a bicategory (synonym for adjunction in bicategories).
* **Lax adjunction**: An adjunction where the unit/counit are not necessarily invertible.
* **∞-adjunction**: An adjunction in an \(\infty\)-category (e.g., a pair of functors with unit/counit satisfying higher coherence).
* **Coend calculus**: The use of coends to express natural transformations and other constructions.
* **Dualizable object**: In a monoidal category, an object \(X\) with dual \(X^*\) and maps \(\text{ev}: X^* \otimes X \to I\), \(\text{coev}: I \to X \otimes X^*\) satisfying zig-zag identities.
* **Fully dualizable object**: In an n-category, an object dualizable in all dualizability dimensions up to n.
* **Serre duality**: In derived categories, an adjunction \(\mathbf{R}\mathcal{H}om(-, \omega) \dashv \mathbf{R}\mathcal{H}om(-, \mathcal{O})\).
* **Verdier duality**: In triangulated categories, an adjunction involving dualizing complexes.
* **Grothendieck duality**: A duality theory for coherent sheaves on schemes.

---

### Monads & Algebras

* **Monad in a bicategory**: A monoid in a bicategory \(\mathcal{B}\): a 1-morphism \(t: c \to c\) with multiplication \(\mu: t \circ t \to t\) and unit \(\eta: 1_c \to t\) satisfying associativity/unitality.
* **Comonad**: The dual of a monad (comonoid in a bicategory).
* **Eilenberg–Moore object**: For a monad \(t\), the universal object of \(t\)-algebras.
* **Kleisli object**: For a monad \(t\), the universal object for free \(t\)-algebras.
* **Distributive law**: A 2-cell \(\lambda: s t \to t s\) for monads \(s, t\) satisfying compatibility conditions.
* **Algebras for a monad**: Pairs \((x, \alpha: t x \to x)\) with \(\alpha \circ \mu_x = \alpha \circ t\alpha\) and \(\alpha \circ \eta_x = 1_x\).
* **Coalgebras**: For a comonad, dual of algebras.
* **Monadic functor**: A functor isomorphic to the forgetful functor from algebras for a monad.
* **Barr–Beck theorem**: Conditions for a functor to be monadic (creation of certain limits and preservation of others).
* **Lax algebra**: An algebra where the structure map \(t x \to x\) is not required to strictly commute with multiplication.
* **Pseudo-monad**: A monad where multiplication and unit are invertible.
* **Pseudo-algebra**: An algebra for a pseudo-monad with invertible structure morphism.

---

### Operads & Algebraic Structures

* **Operad**: A sequence of objects \(O(n)\) with composition, identity, and symmetric group actions.
* **Multicategory**: As defined in classical category theory.
* **PROP**: A symmetric monoidal category with objects \(\mathbb{N}\) and tensor product \(m \otimes n = m+n\).
* **Lawvere theory**: As defined in classical category theory.
* **Topological operad**: An operad enriched in topological spaces.
* **Symmetric operad**: An operad with symmetric group actions on \(O(n)\).
* **Cyclic operad**: An operad with actions of cyclic groups and compatible compositions.
* **Modular operad**: An operad with actions of modular groups (for genus-labeled operations).
* **Algebra over an operad**: For an operad \(O\), an object \(A\) with maps \(O(n) \otimes A^{\otimes n} \to A\) respecting operad structure.
* **Coalgebra over an operad**: Dual of algebra (maps \(A \to O(n) \otimes A^{\otimes n}\)).
* **∞-operad**: An operad in the \(\infty\)-categorical sense (e.g., a dendroidal set with inner horn fillers).
* **Dendroidal set**: A presheaf on the tree category \(\Omega\), modeling operads.
* **Colored operad**: An operad with multiple types (colors) of inputs and outputs.
* **Properad**: An operad-like structure allowing disconnected graphs in compositions.
* **∞-properad**: A properad in \(\infty\)-categories.

---

### Topology & Homotopy Theory

* **Classifying space**: For a group/category, the geometric realization of its nerve.
* **Delooping**: For a group \(G\), a space \(BG\) such that \(\Omega BG \simeq G\).
* **Loop space**: For a pointed space \((X, x_0)\), the space \(\Omega X = \text{Map}_*((S^1, *), (X, x_0))\).
* **Loop space object**: In an \(\infty\)-category, the pullback of a point over itself.
* **Mapping space**: In an \(\infty\)-category, the space \(\text{Map}(x, y)\) of morphisms.
* **Fundamental ∞-groupoid**: The \(\infty\)-groupoid of a space, with objects points, 1-morphisms paths, etc.
* **Homotopy fiber**: For \(f: X \to Y\), the pullback of \(f\) along a path to the basepoint.
* **Homotopy n-type**: A space with trivial homotopy groups above dimension \(n\).
* **Homotopy quotient**: The homotopy colimit of a group action (\(X // G\)).
* **Stabilization**: The process of inverting suspension in a category (e.g., spectra for spaces).
* **Suspension**: For a space \(X\), \(\Sigma X = X \times S^1 / (X \times \{*\} \cup \{*\} \times S^1)\).

---

### Model Structures

* **Model category**: A category with weak equivalences, fibrations, cofibrations satisfying Quillen axioms.
* **Simplicial model category**: A model category enriched over simplicial sets with compatibility axioms.
* **Quillen adjunction**: An adjunction where the left adjoint preserves cofibrations/trivial cofibrations, or equivalently, the right adjoint preserves fibrations/trivial fibrations.
* **Quillen equivalence**: A Quillen adjunction inducing equivalences on homotopy categories.
* **Fibration in model categories**: A morphism satisfying the right lifting property against trivial cofibrations.
* **Cofibration**: A morphism satisfying the left lifting property against trivial fibrations.
* **Weak equivalence**: A morphism inducing isomorphisms in the homotopy category.
* **Left Bousfield localization**: A model structure with the same cofibrations and more weak equivalences.
* **Right Bousfield localization**: A model structure with the same fibrations and more weak equivalences.
* **Monoidal model category**: A model category with a monoidal structure satisfying pushout-product and unit axioms.
* **Enriched model category**: A model category enriched over another model category, with compatibility.
* **Relative category**: A category \(\mathcal{C}\) with a subcategory \(\mathcal{W}\) of weak equivalences.

---

### Advanced Constructions

* **Yoneda embedding for ∞-categories**: A functor \(y: \mathcal{C} \to \mathcal{P}(\mathcal{C})\) preserving limits and fully faithful.
* **Grothendieck construction**: For \(F: \mathcal{C} \to \mathbf{Cat}\), the category \(\int F\) with objects \((c, x)\) where \(c \in \mathcal{C}\), \(x \in Fc\).
* **Straightening and unstraightening**: Equivalence between functors \(\mathcal{C} \to \mathbf{sSet}\) and Cartesian fibrations over \(\mathcal{C}\).
* **Factorization system**: As defined in classical category theory.
* **Orthogonal factorization system**: A factorization system \((\mathcal{E}, \mathcal{M})\) where \(\mathcal{E}\) and \(\mathcal{M}\) are orthogonal.
* **Reflective subcategory**: As defined in classical category theory.
* **Coreflective subcategory**: As defined in classical category theory.
* **Exact ∞-category**: An \(\infty\)-category with finite limits and colimits, and well-behaved exact sequences.
* **Stable ∞-category**: An \(\infty\)-category with finite limits and colimits, where pullback and pushout squares coincide (like triangulated categories).
* **Presentable ∞-category**: A cocomplete \(\infty\)-category with a small generator.
* **Accessible ∞-category**: An \(\infty\)-category with \(\kappa\)-filtered colimits and a set of \(\kappa\)-compact generators.
* **Topos**: A category equivalent to sheaves on a Grothendieck site.
* **Higher topos**: An \(\infty\)-category equivalent to \(\infty\)-sheaves on an \(\infty\)-site.
* **(∞,1)-topos**: A higher topos where morphisms are invertible above dimension 1.
* **(∞,n)-category**: An \(\infty\)-category where k-morphisms are invertible for \(k > n\).
* **Cobordism hypothesis**: A classification of fully extended TQFTs via dualizable objects in symmetric monoidal \((\infty, n)\)-categories.
* **Day convolution**: A monoidal structure on \([\mathcal{C}, \mathcal{V}]\) induced by a monoidal structure on \(\mathcal{C}\).
* **Tannaka duality**: Reconstruction of a group from its category of representations.
* **Twisted arrow category**: For \(\mathcal{C}\), the category with objects morphisms of \(\mathcal{C}\), and morphisms commutative squares.

---

### Dimensional Enhancements

* **2-category**: A category enriched over categories (strict 2-category) or a bicategory (weak).
* **3-category**: A category with 3-morphisms and compositions coherent up to equivalence.
* **n-fold category**: A category internal to (n-1)-fold categories, or a cubical set with compositions.
* **Iterated span category**: A category built by iterating span constructions.
* **Gray-category**: A semi-strict 3-category where interchange is strict up to isomorphism.
* **Trimble n-category**: A definition of n-categories using operads.
* **Tamsamani n-category**: A simplicial definition of weak n-categories.
* **Street nerve**: The nerve of a bicategory (complicial set).
* **Θ-space**: A presheaf on Joyal's cell category \(\Theta\), modeling \((\infty, n)\)-categories.
* **Rezk completion**: The fibrant replacement in the model structure for \(\infty\)-categories.
* **Homotopy coherent nerve**: A functor from simplicial categories to simplicial sets, producing quasicategories.
* **ω-category**: Synonym for omega-category.

---

### Algebraic Geometry & Physics

* **Derived stack**: A stack on the site of simplicial commutative rings or dg-algebras.
* **Higher stack**: A stack taking values in \(\infty\)-groupoids (satisfying descent for hypercovers).
* **Perfect stack**: A derived stack with perfect cotangent complex and affine diagonal.
* **Geometric Langlands program**: A conjectural duality between \(\mathcal{D}\)-modules on Bun_G and sheaves on Loc_{^L G}\).
* **Topological field theory**: A symmetric monoidal functor \(\text{Bord}_n \to \mathcal{C}\).
* **Extended TQFT**: A TQFT defined on higher bordism categories (down to points).
* **Conformal field theory**: A QFT invariant under conformal transformations.
* **Factorization algebra**: A prefactorization algebra satisfying descent for Weiss covers.
* **Chiral algebra**: A vertex algebra with a conformal structure.
* **Vertex operator algebra**: An algebraic structure encoding 2d CFTs.
* **Deformation quantization**: A formal deformation of a commutative algebra into a noncommutative algebra.
* **Drinfeld center**: For a monoidal category \(\mathcal{C}\), the braided monoidal category \(\mathcal{Z}(\mathcal{C})\) of half-braidings.
* **Hochschild cohomology**: For an algebra \(A\), \(\text{HH}^*(A, M) = \text{Ext}_{A \otimes A^{\text{op}}^*(A, M)\).
* **Cyclic homology**: A homology theory for algebras, related to de Rham cohomology.
* **A∞-algebra**: An algebra over the Stasheff operad (associative up to coherent homotopy).
* **A∞-category**: A category enriched over chain complexes with composition associative up to coherent homotopy.
* **L∞-algebra**: A graded vector space with brackets satisfying Jacobi identity up to coherent homotopy.
* **dg-category**: A category enriched over chain complexes.
* **Spectral category**: A category enriched over spectra.
* **Shifted symplectic structure**: A symplectic structure of degree \(k\) on a derived stack.
* **Factorization homology**: An invariant of manifolds with coefficients in \(\mathcal{E}_n\)-algebras.