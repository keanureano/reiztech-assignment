class Branch:
    def __init__(self):
        self.branches = []

    def createBranches(self, amountOfBranches: int):
        for _ in range(amountOfBranches):
            newBranch = Branch()
            self.branches.append(newBranch)


def calculateDepth(branch: Branch) -> int:
    # base case: if the current branch has no child branches, its depth is 1
    if not branch.branches:
        return 1

    # recursive case: the depth of the current branch is 1 plus the maximum depth of its child branches
    maxDepth = 0
    for childBranch in branch.branches:
        childDepth = calculateDepth(childBranch)
        if childDepth > maxDepth:
            maxDepth = childDepth
    
    return maxDepth + 1


def createSampleBranch() -> Branch:
    # create level 1 branch
    root = Branch()

    # create level 2 branches
    root.createBranches(2)

    # create level 3 branches
    root.branches[0].createBranches(1)
    root.branches[1].createBranches(3)

    # create level 4 branches
    root.branches[1].branches[0].createBranches(1)
    root.branches[1].branches[1].createBranches(2)

    # create level 5 branches
    root.branches[1].branches[1].branches[0].createBranches(1)

    return root


def main():
    sampleBranch = createSampleBranch()
    depth = calculateDepth(sampleBranch)
    print(f"Depth of structure: {depth}")


if __name__ == "__main__":
    main()
