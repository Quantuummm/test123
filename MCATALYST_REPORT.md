# MCATalyst Quiz Content Report (Partial Extraction)

Source site: `https://app.mcat-alyst.com/home`

## 1) Topic and game inventory

I extracted all active question metadata from the public `Question` API endpoint used by the app and grouped by `category` and `mode`.

- Total active questions: **1893**

### Chemistry & Physics / Biology & Biochemistry-backed categories and modes

#### `amino_acids` (6 modes)
- `letter-to-name` (20)
- `letter-to-polarity` (19)
- `letter-to-structure` (20)
- `name-to-structure` (20)
- `structure-to-letter` (20)
- `structure-to-name` (20)

#### `amino_acids_characteristics` (2 modes)
- `flashcard` (18)
- `quiz` (20)

#### `functional_groups` (6 modes)
- `multiple_choice` (20)
- `name-to-picture` (57)
- `picture-to-name` (57)
- `single_choice` (115)
- `strong_acids_and_bases` (28)
- `structure-to-IUPAC` (20)

#### `hormones` (11 modes)
- `default` (211)
- `enzyme-inhibitors` (19)
- `enzyme_classifications` (28)
- `flashcard` (20)
- `function-to-name` (38)
- `gland-to-name` (38)
- `multiple_choice` (41)
- `name-to-cause-of-release` (86)
- `name-to-classification` (38)
- `name-to-function` (76)
- `name-to-gland` (38)

#### `metabolism` (6 modes)
- `enzyme-to-reaction` (30)
- `multiple_choice` (30)
- `products` (22)
- `reaction-to-enzyme` (30)
- `single_choice` (54)
- `types_of_organisms` (42)

#### `organic_reactions` (8 modes)
- `function-to-name` (43)
- `functional-groups` (57)
- `identify-the-missing-reactant` (66)
- `identify-the-product` (46)
- `identify-the-product-functional-group` (37)
- `multiple_choice` (43)
- `product-to-reactants` (46)
- `reaction-to-carbon-bond-formed` (27)

#### `units` (9 modes)
- `ceq` (44)
- `default` (51)
- `lenses_and_mirrors` (23)
- `multiple_choice` (20)
- `physics-default` (1)
- `physics-equations` (51)
- `physics_equations` (1)
- `si-prefixes` (18)
- `single_choice` (24)

---

## 2) Fully extracted quiz example: Hormones → Function → Name

Mode key: `hormones | function-to-name`

> Note: For this mode, the API field used for answer feedback (`explanation`) is mostly null/empty, so “feedback” appears as `None` for most items.

1. **Question:** Causes anterior pituitary to release FSH and LH, targeting gonads to release testosterone or estrogen.
   - Choices: GnRH; GHRH; TRH; CRF
   - **Correct answer:** GnRH
   - Feedback: None
2. **Question:** Causes anterior pituitary to release GH (Growth Hormone), which will target bones and muscles to grow.
   - Choices: FSH; GHRH; Prolactin; TSH
   - **Correct answer:** GHRH
   - Feedback: None
3. **Question:** Causes the release of Thyroid hormones (including T3 and T4), helping regulate metabolism and growth rates.
   - Choices: TRH; GH; Oxytocin; LH
   - **Correct answer:** TRH
   - Feedback: None
4. **Question:** Causes the anterior pituitary to release ACTH, which will then stimulate the adrenal cortex to release cortisol.
   - Choices: ADH; CRF; Endorphins; ACTH
   - **Correct answer:** CRF
   - Feedback: None
5. **Question:** Aka dopamine, acts as both a hormone and a neurotransmitter (aka neurohormone) that can inhibit the release of prolactin when released by the hypothalamus, thus preventing milk production.
   - Choices: Melatonin; T3; PIT; T4
   - **Correct answer:** PIT
   - Feedback: None
6. **Question:** Stimulates the maturation of follicles into mature eggs and the maturation of sperm.
   - Choices: FSH; Calcitonin; PTH; Thymosin
   - **Correct answer:** FSH
   - Feedback: None
7. **Question:** The most important hormone in ovulation in females and stimulates the production of androgens, estrogens, and progesterone.
   - Choices: Epinephrine; LH; Norepinephrine; Cortisol
   - **Correct answer:** LH
   - Feedback: None
8. **Question:** Released in response to physiological stress in order for the adrenal cortex to produce cortisol.
   - Choices: ACTH; Aldosterone; Testosterone; Estrogen
   - **Correct answer:** ACTH
   - Feedback: None
9. **Question:** Stimulates the thyroid to release T3 and T4 in order to regulate metabolic rate.
   - Choices: Progesterone; TSH; Insulin; Glucagon
   - **Correct answer:** TSH
   - Feedback: None
10. **Question:** A direct hormone that causes the production of milk in mammary glands.
   - Choices: Prolactin; Somatostatin; Erythropoietin; Calcitriol
   - **Correct answer:** Prolactin
   - Feedback: None
11. **Question:** A direct hormone that serves as a painkiller around the body.
   - Choices: ANP; Endorphins; BNP; Gastrin
   - **Correct answer:** Endorphins
   - Feedback: None
12. **Question:** A direct hormone that promotes muscle, bone, general growth.
   - Choices: Secretin; CCK; GH; Leptin
   - **Correct answer:** GH
   - Feedback: None
13. **Question:** Causes uterine contractions, lactation, social bonding, and sexual reproduction.
   - Choices: Oxytocin; GnRH; GHRH; TRH
   - **Correct answer:** Oxytocin
   - Feedback: None
14. **Question:** Increase the reabsorption of water in the kidneys and stimulates vasoconstriction.
   - Choices: CRF; ADH; PIT; FSH
   - **Correct answer:** ADH
   - Feedback: None
15. **Question:** Regulates circadian rhythm and the sleep/wake cycle.
   - Choices: LH; ACTH; Melatonin; TSH
   - **Correct answer:** Melatonin
   - Feedback: None
16. **Question:** Stimulates growth and metabolic rate through thyroid hormone production.
   - Choices: T3; Prolactin; Endorphins; GH
   - **Correct answer:** T3
   - Feedback: None
17. **Question:** Stimulates growth and metabolic rate through thyroid hormone production.
   - Choices: Oxytocin; ADH; T4; Melatonin
   - **Correct answer:** T4
   - Feedback: None
18. **Question:** Causes decreased blood calcium levels by preventing bone resorption.
   - Choices: Calcitonin; T3; T4; PTH
   - **Correct answer:** Calcitonin
   - Feedback: None
19. **Question:** Regulates blood calcium levels by releasing more calcium from the bones into the blood.
   - Choices: Thymosin; PTH; Epinephrine; Norepinephrine
   - **Correct answer:** PTH
   - Feedback: None
20. **Question:** Helps mature T cells for the immune system.
   - Choices: Cortisol; Aldosterone; Thymosin; Testosterone
   - **Correct answer:** Thymosin
   - Feedback: None
21. **Question:** Fight-or-flight hormone that increases blood flow, oxygen, heart rate, and breathing.
   - Choices: Epinephrine; Estrogen; Progesterone; Insulin
   - **Correct answer:** Epinephrine
   - Feedback: None
22. **Question:** Fight-or-flight hormone that increases vasoconstriction and is a neurotransmitter.
   - Choices: Glucagon; Norepinephrine; Somatostatin; Erythropoietin
   - **Correct answer:** Norepinephrine
   - Feedback: None
23. **Question:** Long term stress hormone that causes your body to shut down long-term projects, increases metabolic rate, increases blood sugar levels, and impacts memory.
   - Choices: Calcitriol; ANP; Cortisol; BNP
   - **Correct answer:** Cortisol
   - Feedback: None
24. **Question:** Regulates blood sodium levels and blood pressure by increasing the reabsorption of sodium in the kidneys and the release of potassium.
   - Choices: Gastrin; Secretin; Aldosterone; CCK
   - **Correct answer:** Aldosterone
   - Feedback: None
25. **Question:** Helps with sexual development and is an anti-aging hormone in males.
   - Choices: Testosterone; Leptin; GnRH; GHRH
   - **Correct answer:** Testosterone
   - Feedback: None
26. **Question:** Stimulates egg development and endometrial development in females.
   - Choices: TRH; CRF; Estrogen; PIT
   - **Correct answer:** Estrogen
   - Feedback: (empty)
27. **Question:** Maintain uterine lining during menstruation and pregnancy.
   - Choices: FSH; Progesterone; LH; ACTH
   - **Correct answer:** Progesterone
   - Feedback: None
28. **Question:** Regulates blood glucose by decreasing it through taking glucose into cells.
   - Choices: TSH; Prolactin; Insulin; Endorphins
   - **Correct answer:** Insulin
   - Feedback: None
29. **Question:** Breaks down glycogen into glucose to increase blood sugar levels.
   - Choices: GH; Glucagon; Oxytocin; ADH
   - **Correct answer:** Glucagon
   - Feedback: None
30. **Question:** Regulates the secretion of hormones like glucagon and insulin in the pancreas and delays gastric emptying.
   - Choices: Melatonin; T3; Somatostatin; T4
   - **Correct answer:** Somatostatin
   - Feedback: None
31. **Question:** Stimulates red blood cell production.
   - Choices: Calcitonin; Erythropoietin; PTH; Thymosin
   - **Correct answer:** Erythropoietin
   - Feedback: None
32. **Question:** Active form of vitamin D that increases blood calcium levels by promoting absorption in the intestines.
   - Choices: Epinephrine; Norepinephrine; Calcitriol; Cortisol
   - **Correct answer:** Calcitriol
   - Feedback: None
33. **Question:** Decrease blood volume and blood pressure.
   - Choices: ANP; Aldosterone; Testosterone; Estrogen
   - **Correct answer:** ANP
   - Feedback: None
34. **Question:** Decreases blood volume, blood pressure, and regulates electrolyte levels.
   - Choices: Progesterone; ANP; Insulin; Glucagon
   - **Correct answer:** ANP
   - Feedback: (empty)
35. **Question:** Stimulates the release of gastric acid in the stomach to help digestion.
   - Choices: Somatostatin; Gastrin; Erythropoietin; Calcitriol
   - **Correct answer:** Gastrin
   - Feedback: None
36. **Question:** Decreases the release of gastric acid in the stomach and stimulates the release of bicarbonate in the pancreas.
   - Choices: ANP; BNP; Secretin; Gastrin
   - **Correct answer:** Secretin
   - Feedback: None
37. **Question:** Stimulates the release of pancreatic enzymes, delays gastric emptying, and contraction of the gallbladder.
   - Choices: CCK; Secretin; Leptin; GnRH
   - **Correct answer:** CCK
   - Feedback: None
38. **Question:** Suppresses appetite and regulates energy balance.
   - Choices: GHRH; TRH; Leptin; CRF
   - **Correct answer:** Leptin
   - Feedback: None

---

## 3) Operational note

The site stores quiz rows behind a public API (`base44.app`), and each row includes:
- `category`
- `mode`
- `question`
- `options`
- `answer`
- `explanation` (feedback field)

For the sampled `function-to-name` mode, `explanation` is mostly null/empty.
