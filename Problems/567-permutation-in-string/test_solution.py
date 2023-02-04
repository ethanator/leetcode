from solution import Solution


def test_solution():
    examples = [
        {
            "input": ["ab", "eidbaooo"],
            "output": True,
        },
        {
            "input": ["ab", "eidboaoo"],
            "output": False,
        },
    ]

    for example in examples:
        assert Solution().checkInclusion(*example["input"]) == example["output"]
