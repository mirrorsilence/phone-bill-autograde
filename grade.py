"""Autograder for the phone-bill task.

Runs four checks on bill() from bill.py and prints feedback a student can act on.
On GitHub Actions it also writes a score table to the run's summary page.
"""
import os
import sys

try:
    from bill import bill
except Exception as error:  # the file does not even import
    print(f"Could not load bill.py: {error}")
    sys.exit(1)

CHECKS = [
    # (minutes, expected, feedback shown when the answer is wrong)
    (0, 2000,
     "With 0 minutes the bill must be just the monthly fee, 2 000 tenge. "
     "Did you forget to add the fee?"),
    (1, 2015,
     "One minute should cost 15 tenge on top of the fee (2 000 + 15 = 2 015). "
     "Check the price per minute."),
    (120, 3800,
     "Aliya's case: 2 000 + 15 x 120 should be 3 800. "
     "Multiply the minutes by 15, then add the fee."),
    (500, 9500,
     "A long month: 2 000 + 15 x 500 should be 9 500. "
     "Your formula works for small numbers only?"),
]


def main() -> int:
    rows = []
    passed = 0
    for minutes, expected, hint in CHECKS:
        try:
            got = bill(minutes)
        except Exception as error:
            got = f"error: {error}"
        ok = got == expected
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] bill({minutes}) -> {got} (expected {expected})")
        if not ok:
            print(f"       Feedback: {hint}")
        rows.append((minutes, got, expected, ok, hint))

    score = f"{passed}/{len(CHECKS)}"
    print(f"\nScore: {score}")
    if passed == len(CHECKS):
        print("All checks passed. Next step: make bill() refuse negative minutes.")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as out:
            out.write(f"## Phone bill autograder: {score}\n\n")
            out.write("| Check | Your answer | Expected | Result | Feedback |\n")
            out.write("|---|---|---|---|---|\n")
            for minutes, got, expected, ok, hint in rows:
                result = "✅ pass" if ok else "❌ fail"
                note = "" if ok else hint
                out.write(f"| bill({minutes}) | {got} | {expected} | {result} | {note} |\n")
            if passed == len(CHECKS):
                out.write("\n**All checks passed.** Next step: make `bill()` refuse negative minutes.\n")

    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
