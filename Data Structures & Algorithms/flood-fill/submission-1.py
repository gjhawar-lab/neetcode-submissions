class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        if initial_color == color:   # already target color — nothing to fill
            return image
        self.fillColor(image, initial_color, color, sr, sc)
        return image

    def fillColor(self, image: List[List[int]], initial_color: int, color: int, sr: int, sc: int) -> None:
        # out of bounds
        if sr < 0 or sr == len(image) or sc < 0 or sc == len(image[0]):
            return
        # not the original color — different color or already filled (acts as visited marker)
        if image[sr][sc] != initial_color:
            return

        image[sr][sc] = color        # color the pixel; prevents revisiting same cell

        self.fillColor(image, initial_color, color, sr + 1, sc)
        self.fillColor(image, initial_color, color, sr - 1, sc)
        self.fillColor(image, initial_color, color, sr, sc + 1)
        self.fillColor(image, initial_color, color, sr, sc - 1)  