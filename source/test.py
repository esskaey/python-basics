import re
from polygon import Polygon


class MathOperations:
    @staticmethod
    def calculate_fibonacci(n: int) -> int:
        """
          F(n) = F(n-1) + F(n-2)

          -> error if n less than zero
          -> if n = 1, return 0
          -> if n == 2 , return 1
          -> if n > 2, then use above formula to return nth fibonacci
        Args:
            n (int): nth fibonacci

        Returns:
            int: sum till nth fibonacci
        """
        pass


class StringOperations:
    url_pattern = (
        r"(?P<root_url>https://[a-zA-Z\-0-9]+\/*svn\/*[a-zA-Z0-9\.*]+)\/*\/*[a-zA-Z0-9\.]*\/*[tags|branches|trunk]+\/*\/*(?P<release_type>Hotfix|ReleaseCandidate)*\/*(?P<project_name>[a-zA-Z\-0-9]+)(Release|\_|\-)(?P<version>[0-9\.]+)"
    )

    @staticmethod
    def get_all_indices(index_string: str) -> list[int]:
        """
        Seperates the indices create a complete list
        -> example string: "1..24,26,27,29" -> Meaning libraries with
        -> index 1 to 24 and libraries with index 26,27,29
        -> creates list of all libraries , ie., 1,2,3,....24,26,27,29
        mandatory input: index_string as shown above
        returns [string] libraries

        Args:
            index_string (str): contains input string pattern, ex. "1..24,26,27,29"

        Returns:
            list[int]: [1,2,3,....24,26,27,29]
        """
        pass

    def get_url_components(self, input_string: str) -> dict:
        """
        Get url components
        returns -> root_url, project_name, version
        """
        regex = re.compile(self.url_pattern)
        re_groups = regex.match(input_string)
        if re_groups is not None:
            return {
                "root_url": re_groups.group("root_url"),
                "project_name": re_groups.group("project_name"),
                "version": re_groups.group("version"),
                "release_type": re_groups.group("release_type"),
            }

        else:
            raise ValueError("--- Invalid URL for parse: {} ---".format(input_string))


class Square(Polygon):
    def __init__(self):
        super().__init__(1)

    def findArea(self):
        return self.sides[0] * self.sides[0]


if __name__ == "__main__":
    n = 10
    # prints a number
    # call the calculate fibonacci method to get output here
    # prints a list of integers
    print(StringOperations.get_all_indices(index_string="1..24,26,29"))
    # match a pattern and return dict
    # test str: "https://server/svn/ProjectA/subcategory/tags/ProjectARelease1.2.3.4"
    StringOperations.get_url_components(
        "https://server/svn/ProjectA/subcategory/tags/ProjectARelease1.2.3.4"
    )

    square = Square()
    square.inputSides()
    print("The area of the square is {}".format(square.findArea()))

    # Write a class implementation for a rectangle
