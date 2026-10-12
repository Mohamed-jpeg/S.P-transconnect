from django.db import migrations


def repair_entreprise_user_fk(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return

    with schema_editor.connection.cursor() as cursor:
        cursor.execute("PRAGMA foreign_keys = OFF")
        cursor.execute(
            """
            CREATE TABLE "EntreprisesApp_entreprise_new" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                "raison_sociale" varchar(200) NOT NULL,
                "matricule_fiscal" varchar(17) NOT NULL UNIQUE,
                "adresse" text NOT NULL,
                "type_entreprise" varchar(100) NOT NULL,
                "created_at" datetime NOT NULL,
                "updated_at" datetime NOT NULL,
                "gerant_id" varchar(8) NOT NULL UNIQUE
                    REFERENCES "EntreprisesApp_utilisateur" ("user_id")
                    DEFERRABLE INITIALLY DEFERRED
            )
            """
        )
        cursor.execute(
            """
            INSERT INTO "EntreprisesApp_entreprise_new" (
                "id", "raison_sociale", "matricule_fiscal", "adresse",
                "type_entreprise", "created_at", "updated_at", "gerant_id"
            )
            SELECT
                "id", "raison_sociale", "matricule_fiscal", "adresse",
                "type_entreprise", "created_at", "updated_at", "gerant_id"
            FROM "EntreprisesApp_entreprise"
            """
        )
        cursor.execute('DROP TABLE "EntreprisesApp_entreprise"')
        cursor.execute(
            'ALTER TABLE "EntreprisesApp_entreprise_new" '
            'RENAME TO "EntreprisesApp_entreprise"'
        )
        cursor.execute("PRAGMA foreign_keys = ON")


class Migration(migrations.Migration):

    dependencies = [
        ("EntreprisesApp", "0003_rename_matricule_fiscale_entreprise_matricule_fiscal_and_more"),
    ]

    operations = [
        migrations.RunPython(repair_entreprise_user_fk, migrations.RunPython.noop),
    ]
