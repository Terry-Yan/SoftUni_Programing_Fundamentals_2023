# def merge_elements(data, start, end):
#     merged_word = ''
#     for i in range(start, end + 1):
#         merged_word += data[i]
#
#     return merged_word
#
#
# def remove_elements(array, start, end):
#     remove_counter = end - start
#     for i in range(remove_counter):
#         array.pop(start)
#
#     return array
#
#
# data_array = input().split()
#
# while True:
#     entry = input().split()
#     command = entry[0]
#
#     if command == "3:1":
#         break
#
#     if command == "merge":
#         start_index = int(entry[1])
#         end_index = int(entry[2])
#
#         start_index = max(0, start_index)
#         end_index = min(len(data_array) - 1, end_index)
#
#         m_element = merge_elements(data_array, start_index, end_index)
#         data_array = remove_elements(data_array, start_index, end_index)
#         data_array.insert(start_index, m_element)
#
# print(data_array)
