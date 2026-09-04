# Database Inspection Report

This report verifies that the required tables (`quiz_exam`, `quiz_question`, and `quiz_choice`) exist in the SQLite database and their schemas correctly correspond to the models as required in Step 5.

## 1. Table: `quiz_exam`

**Status:** Confirmed exists.

**Schema (SQL):**
```sql
CREATE TABLE "quiz_exam" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(200) NOT NULL,
    "description" text NOT NULL,
    "created_at" datetime NOT NULL
)
```

**Columns Verified:**
- `id`: Auto-incrementing primary key.
- `title`: Varchar (200 characters max), required.
- `description`: Text field, required.
- `created_at`: Datetime field, required.

---

## 2. Table: `quiz_question`

**Status:** Confirmed exists.

**Schema (SQL):**
```sql
CREATE TABLE "quiz_question" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "text" text NOT NULL,
    "order" integer unsigned NOT NULL CHECK ("order" >= 0),
    "exam_id" bigint NOT NULL REFERENCES "quiz_exam" ("id") DEFERRABLE INITIALLY DEFERRED
)
```

**Columns Verified:**
- `id`: Auto-incrementing primary key.
- `text`: Text field, required.
- `order`: Unsigned integer, required.
- `exam_id`: Foreign key linked to `quiz_exam`.

---

## 3. Table: `quiz_choice`

**Status:** Confirmed exists.

**Schema (SQL):**
```sql
CREATE TABLE "quiz_choice" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "text" varchar(255) NOT NULL,
    "is_correct" bool NOT NULL,
    "question_id" bigint NOT NULL REFERENCES "quiz_question" ("id") DEFERRABLE INITIALLY DEFERRED
)
```

**Columns Verified:**
- `id`: Auto-incrementing primary key.
- `text`: Varchar (255 characters max), required.
- `is_correct`: Boolean field, required.
- `question_id`: Foreign key linked to `quiz_question`.

---

## Conclusion
All required database tables and their respective columns have been successfully created in `db.sqlite3` and match the expected model definitions.
