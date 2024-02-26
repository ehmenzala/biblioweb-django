from typing import List

PARAGRAPHS_PER_PAGE = 9


def get_line_indices_for_paragraphs(page: int, lines: List[int]) -> List[int]:
    previous_page = page - 1
    start_paragraph = 0 if (page == 1) else (
        previous_page * PARAGRAPHS_PER_PAGE)
    end_paragraph = page * PARAGRAPHS_PER_PAGE
    indices = []

    for i in range(start_paragraph, end_paragraph):
        indices.append(i)
        last_index = len(lines)-1

        if (i == last_index):
            break

        if (i > last_index):
            return []

    return indices
