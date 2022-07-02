"""
Remove all one-line comments,
a comment which starts and ends on one line

Example
Input:
# This is a comment
print('remove_comments')

Output:
print('remove_comments')

Assumption (for this program):
All comments start at the beginning of the line
"""


def remove_comments(lines):
    """
    Input: lines of code as a string
    Returns: lines of code as a string after removing the comments.

    hint:
        Use string methods like split and strip.
        Handle empty lines in code as well.
    """
    # implement your logic here
    l=lines.split('\n')
    for i in l:
        if i:
            if i.find('#')!=-1:
                l.remove(i)
    for i in l:
        if i:
            if i.find('#')!=-1:
                l.remove(i)
                break
    b="\n".join(l)
    return b


