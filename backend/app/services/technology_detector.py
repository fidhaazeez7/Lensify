from app.services.dependency_parser import parse_dependencies
from app.services.project_classifier import classify_project
from app.services.file_analyzer import scan_project


def merge_unique(list1, list2):
    """
    Merge two lists while removing duplicates.
    """
    return sorted(list(set(list1 + list2)))


def detect_technology(project_path: str):
    """
    Technology Detection Engine 2.0

    Combines:
    - Dependency Parser
    - Source Code Scanner
    - Project Classifier
    """

    # Detect from dependency files
    dependency_result = parse_dependencies(project_path)

    # Detect from source code
    scanner_result = scan_project(project_path)

    # Merge results
    technology = {}

    for category in dependency_result.keys():

        technology[category] = merge_unique(
            dependency_result.get(category, []),
            scanner_result.get(category, [])
        )

    project_type = classify_project(project_path)

    return {
        "project_type": project_type,
        "dependencies": technology,
        "technologies": sorted(
            list(
                {
                    tech
                    for values in technology.values()
                    for tech in values
                }
            )
        ),
    }