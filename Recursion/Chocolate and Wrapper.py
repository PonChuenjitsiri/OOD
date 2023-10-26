# inp = input("Enter m, p, w: ").split()
# m, p, w = int(inp[0]), int(inp[1]), int(inp[2])
# def Chocolate(m, p, w):
#     max_warper = int(m/p)
#     res = max_warper
#     while int(max_warper/w) != 0:
#         decimal_part = max_warper/w - int(max_warper/w)
#         if decimal_part >= 0.5:
#             res += int(max_warper/w) + 1
#         else:
#             res += int(max_warper/w)
#         max_warper = int(max_warper/w)
#     print(res)    
# Chocolate(m, p, w)

inp = input("Enter m, p, w: ").split()
m, p, w = int(inp[0]), int(inp[1]), int(inp[2])
def Chocolate(m, p, w, max_warper, res):
    if int(max_warper//w) == 0:
        return print(res)
    decimal_part = max_warper/w - int(max_warper/w)
    if decimal_part >= 0.5:
        res += int(max_warper/w) + 1
    else:
        res += int(max_warper/w)
    max_warper = int(max_warper//w)
    Chocolate(m, p, w, max_warper, res)
Chocolate(m, p, w, int(m//p), int(m//p))
