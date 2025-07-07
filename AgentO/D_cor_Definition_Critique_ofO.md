We are given an extensive list of definitions from category theory and higher category theory. The task is to check each definition for accuracy. Since the list is very long, we will go through each entry and verify if it matches standard mathematical references. We note that some definitions might be slightly informal or have alternative characterizations, but we aim for correctness in the spirit of the term.
We'll break down the list section by section.
### Classical Category Theory
1. **Abelian category**: Correct. Standard definition: additive, has kernels and cokernels, every mono is a kernel, every epi is a cokernel, and the canonical map from coimage to image is an isomorphism.
2. **Additive category**: Correct. Preadditive with zero object and finite biproducts. Hom-sets are abelian groups and composition is bilinear.
3. **Adjoint functor theorem**: Correct. The general adjoint functor theorem requires the solution set condition and that the functor preserves limits (for left adjoint, it would be colimits and cocompleteness). The statement here is for a right adjoint (so F preserves limits) and D complete and locally small with solution set condition.
4. **Adjunction (unit, counit; left and right adjoints)**: Correct. Standard definition with unit and counit satisfying triangle identities.
5. **Automorphism**: Correct. An isomorphism from an object to itself.
6. **Balanced category**: Correct. Every bimorphism (mono and epi) is an isomorphism.
7. **Category (small, large, locally small)**: Correct. Small: objects form a set. Large: objects form a proper class. Locally small: each Hom-class is a set.
8. **Category of elements**: Correct. For a functor F: C → Set, the category of elements has pairs (C, x) and morphisms as described.
9. **Cauchy (Karoubi) completion**: Correct. The completion by splitting idempotents.
10. **Comma category**: Correct. Objects are triples (A, B, f: S(A) → T(B)) and morphisms are pairs making the square commute.
11. **Composition (associativity, identity laws)**: Correct. Standard axioms.
12. **Contravariant functor**: Correct. A functor from the opposite category.
13. **Copower (tensoring with a set or object)**: Correct. In a Set-enriched category, the copower by a set I is the coproduct of I copies of C.
14. **Copresheaf**: Correct. A functor from C to Set (i.e., a presheaf on C^op).
15. **Coproduct**: Correct. Universal cocone.
16. **Cosegment**: Not a standard term. Typically, in the context of biproducts, we have a zero object and injections. But "cosegment" might be a typo or less common. It's dual to "segment", which might refer to the terminal object and projections for product. However, without more context, it's hard to verify. Suggestion: This term is not widely used. The definition given is for a category with finite coproducts: an initial object and two injections from it to the coproduct of two copies of the terminal? But the definition says "0 → 1∐1" which seems to involve the initial and the coproduct of two terminal objects. This is not standard. We might flag this as potentially incorrect or non-standard.
17. **Coslice category**: Correct. Objects are morphisms from A to X.
18. **Coequalizer**: Correct. Universal arrow coequalizing a parallel pair.
19. **Coefficient (in enriched/hyperdoctrine contexts)**: Vague. In enriched categories, the hom-objects are in V, so coefficients would be in V. This is acceptable.
20. **Coend**: Correct. The coend is the coequalizer that coequalizes the left and right actions.
21. **Coreflective subcategory**: Correct. Inclusion has a right adjoint.
22. **Covariant functor**: Correct. Standard functor.
23. **Dinatural transformation**: Correct. Defined by a hexagon condition.
24. **Dual category (opposite category)**: Correct.
25. **End**: Correct. The equalizer defining the end.
26. **Equalizer**: Correct.
27. **Essentially surjective functor**: Correct. Every object in the target is isomorphic to an object in the image.
28. **Exact category**: Correct. An additive category with a class of short exact sequences satisfying Quillen's axioms.
29. **Factorization system**: Correct. (E, M) with factorization, closure, and orthogonality.
30. **Fully faithful functor**: Correct. Induces bijections on Hom-sets.
31. **Functor (covariant, contravariant)**: Correct.
32. **Functor category**: Correct. Objects functors, morphisms natural transformations.
33. **Full functor**: Correct. Surjective on Hom-sets.
34. **Grothendieck fibration**: Correct. Cartesian morphisms exist.
35. **Grothendieck topology**: Correct. Covers satisfy the stated axioms.
36. **Image (regular image, categorical image)**: Correct. The (regular) image is given by the factorization when it exists.
37. **Initial object**: Correct.
38. **Isomorphism**: Correct.
39. **Kan extension (left and right)**: Correct. Universal property stated.
40. **Kernel**: Correct. In an additive category, the equalizer of f and 0.
41. **Lawvere theory**: Correct. A finite product category with objects natural numbers.
42. **Limit (inverse limit, pullback, etc.)**: Correct. Universal cone.
43. **Locally presentable category**: Correct. Cocomplete and accessible (generated under filtered colimits by a set of presentable objects).
44. **Monomorphism**: Correct.
45. **Multicategory**: Correct. Generalization with multiple inputs.
46. **Natural transformation (vertical/horizontal composition)**: Correct.
47. **Natural isomorphism**: Correct.
48. **Nerve of a category**: Correct. Simplicial set with n-simplices as functors from [n].
49. **Opposite category**: Correct.
50. **Power (exponentials, internal homs)**: Correct. In a CCC, the exponential object.
51. **Preadditive category**: Correct. Enriched in abelian groups.
52. **Product**: Correct.
53. **Pullback**: Correct.
54. **Pushout**: Correct.
55. **Reflective subcategory**: Correct. Inclusion has a left adjoint.
56. **Representable functor**: Correct. Isomorphic to Hom(A, -) or Hom(-, A).
57. **Retract (section/retraction)**: Correct. s has a right inverse r.
58. **Slice category**: Correct.
59. **Split exact sequence**: Correct. A short exact sequence that is split, i.e., isomorphic to a direct sum.
60. **Split monomorphism / split epimorphism**: Correct. A mono that has a left inverse, an epi with a right inverse.
61. **Subobject (subobject classifier in a topos)**: Correct. In a topos, subobjects are classified by a morphism to Ω.
62. **Terminal object**: Correct.
63. **Universal arrow / universal property**: Correct. Defined via factorization.
64. **Weak limit / weak colimit**: Correct. Universal up to isomorphism, not necessarily unique.
65. **Zero object**: Correct. Initial and terminal.
66. **Zero morphism**: Correct. Factors through zero object.
### Basic Higher Category Concepts
67. **∗Complicial set**: Correct. A stratified simplicial set with complicial horn filling.
68. **Cellular set**: This term is less common. It might refer to a presheaf on globes, but typically "globular set" is used. The definition says "presheaf on the category of globes", which is a globular set. However, "cellular set" is not standard. It might be a typo or an alternative name. Flag as potentially non-standard.
69. **Homotopy category**: Correct. Obtained by inverting weak equivalences.
70. **n-category**: Correct. Enriched in (n-1)-categories.
71. **∞-category**: Correct. Weak n-category for all n.
72. **Weak n-category**: Correct. Coherent higher equivalences.
73. **Strict n-category**: Correct. Strict equalities.
74. **Bicategory**: Correct. Weak 2-category.
75. **Globular set**: Correct. Presheaf on the globe category.
76. **Nerve of a category**: Repeated. Already in classical.
77. **Quasicategory**: Correct. Simplicial set with inner horn fillers.
78. **Kan complex**: Correct. All horns fill.
79. **Simplicial set**: Correct.
80. **Complete Segal space**: Correct. Simplicial space satisfying Segal and completeness.
81. **Segal category**: Correct. Simplicial object with discrete 0-simplices and Segal conditions.
82. **Homotopy hypothesis**: Correct. ∞-groupoids equivalent to spaces.
### Types of Higher Categories
83. **Cartesian closed category**: Correct. Finite products and exponentials.
84. **Closed category**: Correct. Monoidal with right adjoints to tensor.
85. **Compact closed category**: Correct. Every object has a dual.
86. **Double category**: Correct. Objects, horizontal and vertical morphisms, and squares.
87. **Enriched category**: Correct. Hom-objects in a monoidal category.
88. **Internal category**: Correct. Category object in another category.
89. **Monoidal category**: Correct. Tensor product, unit, associator, unitor.
90. **Braided monoidal category**: Correct. Braiding with hexagons.
91. **Monoidal ∞-category**: Correct. ∞-category with monoidal structure.
92. **Omega-category (ω-category)**: Correct. Weak n-category for all n.
93. **Pivotal category**: Correct. Rigid with monoidal natural isomorphism to double dual.
94. **Fusion category**: Correct. Semisimple, rigid, finitely many simples, over algebraically closed field.
95. **Modular tensor category**: Correct. Ribbon fusion with non-degenerate braiding.
96. **Symmetric monoidal category**: Correct. Braiding is symmetric.
97. **Virtual double category**: Correct. Generalization of double categories.
### Morphisms & Cells
98. **k-morphism**: Correct.
99. **2-morphism**: Correct.
100. **Higher morphism**: Correct.
101. **Globular k-cell**: Correct.
102. **Icon**: Correct. Identity-component oplax natural transformation.
103. **Lax natural transformation**: Correct. With 2-cells for composition.
104. **Oplax natural transformation**: Correct. Dual to lax.
105. **Pseudonatural transformation**: Correct. With invertible 2-cells.
106. **Modification**: Correct. 3-cell between pseudonatural transformations.
107. **Equivalence in higher categories**: Correct. Invertible up to higher equivalences.
108. **Adjoint equivalence**: Correct. Equivalence with unit and counit satisfying triangles.
### Functors & Transformations
109. **∞-functor**: Correct. Preserves composition up to coherent homotopy.
110. **Functor between bicategories**: Correct. Pseudofunctor, lax, oplax, or strict.
111. **Homotopy coherent diagram**: Correct. Diagram with specified homotopies for coherence.
112. **Lax functor**: Correct. Preserves composition and identity up to non-invertible cells.
113. **Oplax functor**: Correct. Dual.
114. **Pseudofunctor**: Correct. Lax with invertible comparison cells.
115. **Transformation between ∞-functors**: Correct. 1-simplex in mapping space.
116. **Natural isomorphism up to higher equivalence**: Correct. Components are equivalences.
### Limits & Colimits
117. **Homotopy colimit**: Correct. Colimit in the homotopy sense.
118. **Homotopy limit**: Correct.
119. **∞-categorical colimit**: Correct. Universal cocone defined via mapping spaces.
120. **∞-categorical limit**: Correct.
121. **Weighted limit**: Correct. Limit with weight.
122. **Bicolimit**: Correct. Colimit universal up to equivalence.
123. **Flexible limit**: Correct. 2-categorical limit universal up to equivalence.
124. **Kan extension in higher categories**: Correct. ∞-categorical Kan extension.
125. **Lax limit**: Correct. Limit with lax cones.
126. **Pseudolimit**: Correct. Bilimit with invertible 2-cells.
127. **End (as a limiting construction)**: Correct. Enriched end.
128. **Bilimit**: Correct. Bicategorical limit.
### Adjunctions & Duality
129. **Adjunction in bicategories**: Correct. Unit and counit 2-cells satisfying triangle identities up to isomorphism.
130. **Biadjunction**: Correct. Adjunction in a tricategory.
131. **Lax adjunction**: Correct. With one lax and one oplax functor.
132. **∞-adjunction**: Correct. Adjunction in ∞-category.
133. **Coend calculus**: Correct. Calculus of coends.
134. **Dualizable object**: Correct. Has dual with evaluation and coevaluation.
135. **Fully dualizable object**: Correct. Dualizable at all levels.
136. **Serre duality**: Correct. Duality on coherent sheaves.
137. **Verdier duality**: Correct. Duality in derived category.
138. **Grothendieck duality**: Correct. Duality for morphisms of schemes.
### Monads & Algebras
139. **Monad in a bicategory**: Correct. Endomorphism with multiplication and unit.
140. **Comonad**: Correct. Dual.
141. **Eilenberg–Moore object**: Correct. Universal for algebras.
142. **Kleisli object**: Correct. Universal for free algebras.
143. **Distributive law**: Correct. 2-cell between monads.
144. **Algebras for a monad**: Correct.
145. **Coalgebras**: Correct.
146. **Monadic functor**: Correct. Equivalent to forgetful from algebras.
147. **Barr–Beck theorem**: Correct. Monadicity theorem.
148. **Lax algebra**: Correct. Algebra with non-invertible structure maps.
149. **Pseudo-monad**: Correct. Monad with equivalences.
150. **Pseudo-algebra**: Correct. Algebra with invertible structure up to cells.
### Operads & Algebraic Structures
151. **Operad**: Correct.
152. **Multicategory**: Repeated.
153. **PROP**: Correct. Monoidal category with objects naturals.
154. **Lawvere theory**: Repeated.
155. **Topological operad**: Correct.
156. **Symmetric operad**: Correct.
157. **Cyclic operad**: Correct.
158. **Modular operad**: Correct.
159. **Algebra over an operad**: Correct.
160. **Coalgebra over an operad**: Correct.
161. **∞-operad**: Correct.
162. **Dendroidal set**: Correct. Presheaf on dendroidal category.
163. **Colored operad**: Correct.
164. **Properad**: Correct.
165. **∞-properad**: Correct.
### Topology & Homotopy Theory
166. **Classifying space**: Correct. BG for a group or category.
167. **Delooping**: Correct. BX such that ΩBX ≃ X.
168. **Loop space**: Correct.
169. **Loop space object**: Correct. In a pointed ∞-category.
170. **Mapping space**: Correct. Hom in ∞-category.
171. **Fundamental ∞-groupoid**: Correct.
172. **Homotopy fiber**: Correct.
173. **Homotopy n-type**: Correct.
174. **Homotopy quotient**: Correct. X//G.
175. **Stabilization**: Correct. Passage to spectra.
176. **Suspension**: Correct.
### Model Structures
177. **Model category**: Correct. Cofibrations, fibrations, weak equivalences.
178. **Simplicial model category**: Correct. Enriched over simplicial sets with compatibility.
179. **Quillen adjunction**: Correct. Adjunction with left adjoint preserving cofibrations and trivial cofibrations.
180. **Quillen equivalence**: Correct. Induces equivalence on homotopy categories.
181. **Fibration in model categories**: Correct.
182. **Cofibration**: Correct.
183. **Weak equivalence**: Correct.
184. **Left Bousfield localization**: Correct. New model structure by adding weak equivalences.
185. **Right Bousfield localization**: Correct. Dual.
186. **Monoidal model category**: Correct. Monoidal structure compatible with model structure.
187. **Enriched model category**: Correct.
188. **Relative category**: Correct. Category with a subcategory of weak equivalences.
### Advanced Constructions
189. **Yoneda embedding for ∞-categories**: Correct. Functor to presheaves of spaces.
190. **Grothendieck construction**: Correct. Equivalence between functors to Cat_∞ and (co)cartesian fibrations.
191. **Straightening & unstraightening**: Correct. Quillen equivalence.
192. **Factorization system**: Correct. In ∞-category, with orthogonality.
193. **Orthogonal factorization system**: Correct. Factorization system with unique lifting.
194. **Reflective subcategory**: Correct. Inclusion has left adjoint.
195. **Coreflective subcategory**: Correct. Inclusion has right adjoint.
196. **Exact ∞-category**: Correct. Barwick's definition.
197. **Stable ∞-category**: Correct. Pointed, finite limits and colimits, suspension equivalence.
198. **Presentable ∞-category**: Correct. Accessible and cocomplete.
199. **Accessible ∞-category**: Correct. Accessible.
200. **Topos**: Correct. Elementary topos: cartesian closed, subobject classifier, finite limits, and colimits? Actually, elementary topos has finite limits and power objects (hence cartesian closed) and a subobject classifier. It does not necessarily have all colimits, but the definition here says "finitely complete, has all small colimits", which is a Grothendieck topos. The term "topos" here is defined as Grothendieck topos, but note that "elementary topos" is more general. However, the definition given matches Grothendieck topos. But the term is "Topos", which might be ambiguous. The definition says: "finitely complete, has all small colimits, locally cartesian closed, and possesses a subobject classifier". This is actually a characterization of Grothendieck toposes (by Giraud's theorem). However, note that Grothendieck toposes are locally cartesian closed and have a subobject classifier. So it's correct for Grothendieck toposes. But the term "elementary topos" does not require cocompleteness. So we note that the definition given is for a Grothendieck topos, not an elementary topos. Since the term is "Topos", it might be intended as Grothendieck. But to be precise, we should note that in the context of this list, it's defined as such.
201. **Higher topos / (∞,1)-topos**: Correct. Presentable ∞-category that is a left exact localization of presheaves.
202. **(∞,n)-category**: Correct. Weak n-category with invertible higher morphisms above n.
203. **Cobordism hypothesis**: Correct. Fully extended TQFTs classified by fully dualizable objects.
204. **Day convolution**: Correct. Monoidal structure on presheaves.
205. **Tannaka duality**: Correct. Reconstruction from representations.
206. **Twisted arrow category**: Correct. For 1-category, morphisms as objects, squares as morphisms. In ∞-context, homotopy coherent.
### Additional Terms (from the table)
207. **2-category**: Correct. Enriched in Cat.
208. **3-category**: Correct. Enriched in 2-Cat.
209. **n-fold category**: Correct. Iterated internal category.
210. **Iterated span category**: Correct. Composed of spans.
211. **Gray-category**: Correct. Semi-strict 3-category.
212. **Trimble n-category**: Correct. Defined via operads.
213. **Tamsamani n-category**: Correct. Simplicial approach.
214. **Street nerve**: Correct. Nerve for 2-categories.
215. **Θ-space**: Correct. Presheaf on Θ_n.
216. **Rezk completion**: Correct. Fibrant replacement for Segal spaces.
217. **Homotopy coherent nerve**: Correct. From simplicial categories to quasicategories.
218. **ω-category (omega)**: Correct. Strict ∞-category.
### More Terms (from the second table)
219. **Derived stack**: Correct. Stack on simplicial commutative rings.
220. **Higher stack**: Correct. Stack of ∞-groupoids.
221. **Perfect stack**: Correct. With compactly generated quasi-coherent sheaves.
222. **Geometric Langlands program**: Correct. Correspondence.
223. **Topological field theory (TFT)**: Correct.
224. **Extended TQFT**: Correct.
225. **Conformal field theory (CFT)**: Correct.
226. **Factorization algebra**: Correct. Prefactorization cosheaf with factorization.
227. **Chiral algebra**: Correct. Sheaf of Lie algebras with chiral operation.
228. **Vertex operator algebra (VOA)**: Correct.
229. **Deformation quantization**: Correct.
230. **Drinfeld center**: Correct. Center of monoidal category.
231. **Hochschild cohomology**: Correct.
232. **Cyclic homology**: Correct.
233. **A_∞-algebra**: Correct.
234. **A_∞-category**: Correct.
235. **L_∞-algebra**: Correct.
236. **dg-category**: Correct.
237. **Spectral category**: Correct.
238. **Shifted symplectic structure**: Correct.
239. **Factorization homology**: Correct.
### Summary of Potential Issues
- **Cosegment**: Definition seems non-standard. Typically, in a category with finite coproducts, we have an initial object and coproducts, but the specific "cosegment" as defined (initial object and two injections to the coproduct of two copies of the terminal) is not a common term. It might be intended for a bipointed category, but without more context, it's unclear. We flag this as potentially incorrect or requiring clarification.
- **Cellular set**: The term is not standard. The definition matches "globular set", so it might be a typo.
- **Topos**: The definition given is for a Grothendieck topos (having all small colimits), but note that elementary toposes do not necessarily have all colimits. Since the definition specifies "has all small colimits", it is correct for Grothendieck toposes. But the term "topos" without qualification might be ambiguous. However, in the context of advanced constructions, it's likely intended as Grothendieck.
Other definitions appear to be correct.
Therefore, the only two definitions that stand out as potentially problematic are "Cosegment" and "Cellular set". The rest are accurate.