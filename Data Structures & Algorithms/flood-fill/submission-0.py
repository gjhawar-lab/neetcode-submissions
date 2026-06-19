class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited_set = set()
        initial_color = image[sr][sc]
        wanted_color = color
        self.fillColor(image, initial_color, wanted_color, visited_set, sr, sc)
        return image

    def fillColor(self, image: List[List[int]], initial_color, wanted_color, visited_set, sr, sc) -> List[List[int]]:

        # Bound and visit checks
        if min(sr,sc) < 0 or sr == len(image) or sc == len(image[0]) or (sr,sc) in visited_set or image[sr][sc] == wanted_color :
            return image
        
        # add to visited set
        visited_set.add((sr, sc))

        # color if same as initial node
        if image[sr][sc] == initial_color:
            image[sr][sc] = wanted_color
        else: 
            return

        self.fillColor(image, initial_color, wanted_color, visited_set, sr + 1, sc)
        self.fillColor(image, initial_color, wanted_color, visited_set, sr - 1, sc)
        self.fillColor(image, initial_color, wanted_color, visited_set, sr, sc + 1)
        self.fillColor(image, initial_color, wanted_color, visited_set, sr, sc - 1)
        
        # remove from visited set
        visited_set.remove((sr,sc))

        return image   