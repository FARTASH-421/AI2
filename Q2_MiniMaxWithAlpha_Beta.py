# def minimax_alpha_beta(lis, depth, alpha, beta, maximizing_player, evaluation_function):
#
#     if len(lis) < 2:
#             return lis[0], str(lis[0])
#
#     if maximizing_player:
#         max_val = -float('inf')
#         LC = []
#         RL = []
#         index = int(len(lis)/2)
#         j = index
#         for i in range(index):
#             LC.append(lis[i])
#             RL.append(lis[j])
#             j += 1
#         if j < len(lis):
#         RL.append(lis[j])
#         for child in node.generate_children():
#             val = minimax_alpha_beta(child, depth - 1, alpha, beta, False, evaluation_function)
#             max_val = max(max_val, val)
#             alpha = max(alpha, val)
#             if beta <= alpha:
#                 break
#         return max_val
#     else:
#         min_val = float('inf')
#         for child in node.generate_children():
#             val = minimax_alpha_beta(child, depth - 1, alpha, beta, True, evaluation_function)
#             min_val = min(min_val, val)
#             beta = min(beta, val)
#             if beta <= alpha:
#                 break
#         return min_val