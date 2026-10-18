# AI Log - Workshop TransConnect (Jalon 1)

## Entrée 1 - [Insert Today's Date]
* **Outil IA utilisé** : Gemini
* **Prompt**: "Fix and generate the Offre model according to requirements"
* **Output Summary**: Corrected Offre model structure.
* **Identified Discrepancies vs Specs (4 Anomalies)**:
  1. `prix`: Originally `CharField(max_length=10)`, changed to `DecimalField` for monetary accuracy.
  2. `delai_jours`: Originally `IntegerField`, changed to `PositiveIntegerField` since delivery time cannot be negative.
  3. `statut`: Added `choices=STATUT_CHOICES` and set `default='proposee'`.
  4. `date_proposition`: Changed `auto_now=True` to `auto_now_add=True` to store the creation date rather than updating on every save.
* **Corrections & Justification**: Fully updated `OffresApp/models.py` to conform to the ORM field requirements specified in the workshop instructions.


## Entrée 1 - [Oct 18 2026]
* **Outil IA utilisé** : Copilot
* **Prompt**: "Fix and explain why i cant add offres"
* **Output Summary**: Diagnosed and fixed the validation error preventing the creation of offers.
* **Main Cause**: `Offre.clean()` only allows offers for expeditions whose status is `publie`. The selected expedition had another status, so Django raised `ValidationError: Cette expédition n'est plus ouverte aux offres.`
* **Additional Corrections**:
  1. Validated an offer before changing its expedition to `attribuee`, so accepted offers can be saved correctly.
  2. Fixed the duplicate-offer query to use `expedition_id` and `transporteur_id`.
  3. Applied duplicate-offer validation to new offers as well as existing offers.
  4. Corrected automatically generated expedition references to use the required `EXP-YY-NNNNN` format.
* **Result**: New offers can be created when the expedition is published; closed expeditions are correctly rejected.