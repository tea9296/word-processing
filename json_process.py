from typing import Callable, Union, Tuple
import json, re
import os, traceback


def extract_json(s) -> Union[dict, None]:
    """parse the JSON part of the string

    Args:
        s (str): string that contains JSON part

    Returns:
        Union[dict, None]: return the JSON part of the string, if not found return None
    """
    # Use a regular expression to find the JSON part of the string
    match = re.search(r'\{[\s\S]*\}', s)
    if match:
        json_part = match.group(0)
        try:
            # Try to parse the JSON part of the string
            return json.loads(json_part)
        except json.JSONDecodeError:
            traceback.print_exc()
            print("The JSON part of the string is not well-formatted")
            return None
    else:
        print("No JSON found in the string")
        return None
