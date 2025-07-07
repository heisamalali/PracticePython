# using  # we can define a set .
# set is type of collection which we can not add repetitive values
peopleSet = {"a", "b", "c"}
richPeopleSet = {"a"}
poorPeopleSet = peopleSet.difference(richPeopleSet)
allPeopleSet = poorPeopleSet.union(richPeopleSet)
print(poorPeopleSet)

studyMathSet = {"a", "b", "c", "d", "e", "f", "g", "h"}
studyArtSet = {"a","h","n"}
studyBoth = studyMathSet.intersection(studyArtSet)
print(studyBoth)

# for list we can use []
peopleList = ["a", "b", "c", "d", "e", "f", "g", "h"]
peopleList.append("i")

# with tuple we can use ()
peopleTuple = ("a","b")
