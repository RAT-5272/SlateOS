# Naming Conventions
### Rough priority list
<small>(Lower is higher)</small>
- flatcase
- snake_case
- camelCase
- PascalCase
- FULLCASE (unused)
- SCREAMING_SNAKE_CASE

## Encouraged practices
- Modules and submodules: PascalCase.PascalCase (e.g. Renderer.Interface)
- Types: PascalCase (Structs, enums, generics, classes, or normal types) (e.g. DatabaseManager)
- Functions: PascalCase (e.g. LoadFilesFromPath)
- Variables
 - Short term: snake_case (e.g. iterators, this is just optional though) (e.g. i, slot_index)
 - Regular variables: camelCase
 - Constants: SCREAMING_SNAKE_CASE
- Types / extra placed AFTER variable name (hungarian notation, optional): variableName_PascalCase (e.g. UnrollAndFMA_512)
- If something is private, it should be prepended with an underscore.

## Comments & Documentation
"""
Documentation comments should ideally be used in nearly every function or class, they are placed at the beginning and detail what the function does at a high level, as well as what is inputted or returned.
"""
#Inline comments give some information about what the code around it is doing

### Full Example Styled Code
def SieveOfEratosthened_Naive(n: int) -> list[int]:
    """
    """