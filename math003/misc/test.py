import math, enum, re

ratio = 2**(0.5)
b_start_height = ratio
b_start_width = 1
a_start_height = 2**(0.25)
a_start_width = 1/a_start_height

class PaperSizeType(enum.Enum):
    A = 0
    B = 1

class ISOPaper:
    def __init__(self) -> None:
        self.width = b_start_width
        self.height = b_start_height
        self.size = 0
        # self.size_num = 0
    
    def __repr__(self) -> str:
        return f"WH {self.width}m x {self.height}m ({self.name})"
    
    @property
    def name(self) -> str:
        size_num, size_index = divmod(self.size, 2)
        size_name = ["B", "A"][size_index]
        if size_num < 0:
            return f"{abs(size_num) + 1}{size_name}0"
        return f"{size_name}{size_num}"

    def _update(self) -> "ISOPaper":
        size_num, size_index = divmod(self.size, 2)

        if size_index == 0: # B
            self.width = b_start_width / (2**size_num / ratio**size_num)
        elif size_index == 1: # A
            self.width = a_start_width / (2**size_num / ratio**size_num)
        
        self.height = self.width * ratio
        return self
    
    def set_size_str(self, size: str) -> "ISOPaper":
        m = re.match(r"(\d+)?([abAB])(?:\s+)?(\d+)", size)
        size_1 = m.group(1) or 1
        size_name = m.group(2)
        size_2 = m.group(3) or 0
        self.size = ((int(size_1) - 1) * -2) + (int(size_2) * 2) + (1 if size_name.upper() == "A"
                                                                    else 0)
        return self._update()
    
    def upsize(self, times: int = 1) -> "ISOPaper":
        self.size -= times
        return self._update()
    
    def downsize(self, times: int = 1) -> "ISOPaper":
        self.size += times
        return self._update()

    # def downsize(self, times: int = 1) -> "ISOPaper":
    #     self.size += 1
    #     downsize_amount, flip_type = divmod(times, 2)
    #     self.size_num += downsize_amount
    #     if flip_type:
    #         if self.size_type is PaperSizeType.B:
    #             self.size_type = PaperSizeType.A
    #         else:
    #             self.size_type = PaperSizeType.B
    #     return self._update()

    # def upsize(self, times: int = 1) -> "ISOPaper":
    #     upsize_amount, flip_type = divmod(times, 2)
    #     self.size_num -= upsize_amount
    #     if flip_type:
    #         if self.size_type is PaperSizeType.B:
    #             self.size_type = PaperSizeType.A
    #         else:
    #             self.size_type = PaperSizeType.B
    #     return self._update()


    # def down(self, times: int) -> None:
    #     if self.size_type is PaperSizeType.A:

    #     self.width = self.width / (2**times / ratio**times)
    #     self.height = self.width * ratio
    
    # def up(self, times: int) -> None:
    #     self.width = self.width / (ratio**times / 2**times)
    #     self.height = self.width * ratio


p = ISOPaper()
print(p.set_size_str("A231"))
# print(p.set_size_str("2A0"))
# print(p.downsize(375))
# p.size = -1
# p._update()
# print(p)
# print(p)
# p.size = -1
# print(p._update())
# p.size_num = -1
# p.size_type = PaperSizeType.A
# print(p._update())
# print(p)
# p.down(4)
# print(p)
# p.up(4)
# print(p)





# print(p)
# p.down(1)
# print(p)
# p.up(1)
# print(p)
# a = A()
# a.shrink(231)
# print(a.size)


