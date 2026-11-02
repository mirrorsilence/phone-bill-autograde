# Phone-bill autograder: live demo

A tiny GitHub repository that scores a student's code automatically and gives
feedback every time the student pushes. It is the live demo for the
presentation "Automated Scoring & Feedback".

**The task (same as in the warm-up):** Aliya's phone plan costs 2 000 ₸ a month
plus 15 ₸ for every minute. Write `bill(minutes)` in `bill.py`.

## What is inside

| File | What it does |
|---|---|
| `bill.py` | The student's file. It starts with a mistake (no monthly fee). |
| `grade.py` | The autograder: 4 checks, each with a feedback message. |
| `.github/workflows/autograde.yml` | Tells GitHub to run `grade.py` on every push. |
| `demo_versions/` | Three ready versions to paste into `bill.py` during the demo. |

## Set up (once, about 5 minutes, the day before)

1. On github.com click **New repository**, name it `phone-bill-autograde`, make it **Public**, create it.
2. Click **uploading an existing file** and drag in everything from this folder,
   including the hidden `.github` folder. If the browser hides it, create the file
   manually: **Add file → Create new file**, name `.github/workflows/autograde.yml`,
   and paste the contents.
3. Open the **Actions** tab. If GitHub asks, click **I understand my workflows, enable them**.
4. Make one test edit to `bill.py` and commit. A yellow dot, then a red ✗, should appear.
   Your demo is ready.

## Live demo script (4 minutes)

1. **Show the task** in `bill.py`. Ask the room: "What is wrong with this code?"
2. **Version 1 (forgot the fee):** commit as is. Open **Actions → the latest run → Summary**.
   Score **0/4**, with a feedback line for each check.
3. **Version 2 (hard-coded):** paste `demo_versions/2_hardcoded.py` into `bill.py` and commit.
   It passes Aliya's case (120 minutes) but fails the others. Score **2/4**.
   Point: you can't fool the machine if the tests cover several cases.
4. **Version 3 (correct):** paste `demo_versions/3_correct.py` and commit.
   Score **4/4**, with a next step: "make bill() refuse negative minutes".
5. Tie back: the feedback was written once by the teacher and is sent to every student instantly.

**Backup if the Wi-Fi fails:** run `python grade.py` on your laptop; it prints the same feedback.

## Note on GitHub Classroom

GitHub Classroom was retired on 28 August 2026. This demo uses plain
GitHub Actions, which still works in any repository. For whole classes, GitHub
points to Classroom 50 (free, open source, from the CS50 team) and Codio.

---

## Кратко по-русски

1. Создайте публичный репозиторий на GitHub и загрузите все файлы, включая папку `.github`.
2. Во вкладке **Actions** включите workflows.
3. На демо: меняйте содержимое `bill.py` на версии из `demo_versions/` (1 → 2 → 3),
   после каждого коммита открывайте **Actions → последний запуск → Summary**.
   Оценки: 0/4, 2/4, 4/4, и у каждой ошибки есть своя подсказка.
4. Если нет интернета: `python grade.py` на ноутбуке выдаёт ту же обратную связь.
