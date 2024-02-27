from typing import List
import math


def get_line_indices_for_paragraphs(page: int, lines: List[int], paragraphs_per_page: int) -> List[int]:
    previous_page = page - 1
    start_paragraph = 0 if (page == 1) else (
        previous_page * paragraphs_per_page)
    end_paragraph = page * paragraphs_per_page
    indices = []

    for i in range(start_paragraph, end_paragraph):
        indices.append(i)
        last_index = len(lines)-1

        if (i == last_index):
            break

        if (i > last_index):
            return []

    return indices


def get_list_of_total_pages(lines: List[int], paragraphs_per_page: int) -> int:
    raw_total_pages = len(lines) / paragraphs_per_page
    total_pages = math.ceil(raw_total_pages)
    return range(1, total_pages + 1)
