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