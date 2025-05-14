# Conflict Resolution Notes

## Conflict Details

-   **Branches Involved**: `feature-a` and `feature-b`
-   **File Affected**: `main.py`
-   **Function Affected**: `load_users`
-   **Conflict Description**:
    -   In `feature-a`, the `load_users` function was modified to display users in a tabulated format with asterisks, aligning fields with fixed spacing.
    -   In `feature-b`, the same function was modified to display users in a boxed format with dashes, using a pipe-separated layout.
    -   The conflict occurred because both branches modified the same lines of the `load_users` function, resulting in a merge conflict when attempting to merge `feature-a` into `feature-b`.

## Resolution Decision

-   **Approach**: Instead of choosing one format over the other, I combined both functionalities into a single `load_users` function that supports both display styles.
-   **Implementation**:
    -   Added a `style` parameter to the `load_users` function with two options: `'boxed'` (from `feature-b`) and `'tabulated'` (from `feature-a`).
    -   Modified the function to use conditional logic to render the appropriate format based on the `style` parameter.
    -   Updated the `main` function and `argparse` to accept a `--style` command-line argument with choices `'boxed'` or `'tabulated'`, defaulting to `'boxed'`.
    -   Retained a fallback default format (from the original `develop` branch) for invalid style inputs.
-   **Rationale**:
    -   Combining both features preserves the work done in both branches, enhancing the program's flexibility.
    -   Users can now choose their preferred display style via a command-line argument, improving usability.
    -   The solution avoids discarding either implementation, aligning with the goal of integrating both features.

## Testing

-   Tested the program with:
    -   `python main.py --style boxed`: Displays users in the boxed format with dashes.
    -   `python main.py --style tabulated`: Displays users in the tabulated format with asterisks.
    -   `python main.py`: Defaults to boxed format.
-   Verified that CSV loading, sorting, and HTML report generation remain unaffected.

## Commit

-   The resolved code was committed with the message: "Resolve merge conflict in load_users by combining boxed and tabulated formats".
