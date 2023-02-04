from solution import Solution


def test_solution():
    examples = [
        {
            "input": [
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "fine"], ["drama", "acting"],["skills", "talent"]],
            ],
            "output": True,
        },
        {
            "input": [
                ["great"],
                ["great"],
                [],
            ],
            "output": True,
        },
        {
            "input": [
                ["great"],
                ["doubleplus", "good"],
                [["great", "doubleplus"]],
            ],
            "output": False,
        },
    ]

    for example in examples:
        assert Solution().areSentencesSimilar(*example["input"]) == example["output"]
