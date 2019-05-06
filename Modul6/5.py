class MhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = MhsTIF('Susi', 20, 'Bojonegoro', 5000000)
c1 = MhsTIF('Triana', 5, 'Sragen', 2000000)
c2 = MhsTIF('Wati', 20, 'Surakarta', 4500000)
c3 = MhsTIF('Andra', 88, 'Sukoharjo', 935000)
c4 = MhsTIF('Ika', 41, 'Boyolali', 2900000)
c5 = MhsTIF('Andi', 12, 'Solo', 3500000)
c6 = MhsTIF('Eni', 10, 'Klaten', 5450000)
c7 = MhsTIF('Salsa', 67, 'Malang', 8450000)
c8 = MhsTIF('Anto', 26, 'Klaten', 2350000)
c9 = MhsTIF('Ali', 45, 'Karanganyar', 4700000)
c10 = MhsTIF('Jaki', 22, 'Solo', 7650000)

daftar = [c0.no, c1.no, c2.no, c3.no, c4.no, c5.no, c6.no, c7.no, c8.no, c9.no, c10.no]

def _merge_sort(indices, the_list):
    start = indices[0]
    end = indices[1]
    half_way = (end - start) // 2 + start
    
    if start < half_way:
        _merge_sort((start, half_way), the_list)

    if half_way + 1 <= end and end - start != 1:
       _merge_sort((half_way + 1, end), the_list)

    sort_sub_list(the_list, indices[0], indices[1])
    
    return the_list
    
    
def sort_sub_list(the_list, start, end):
    orig_start = start
    initial_start_second_list = (end - start)//2 + start + 1
    list2_first_index = initial_start_second_list
    new_list = []
    
    while start < initial_start_second_list and list2_first_index <= end:
        first1 = the_list[start]
        first2 = the_list[list2_first_index]
        if first1 > first2:
            new_list.append(first2)
            list2_first_index += 1
        else:
            new_list.append(first1)
            start += 1
            
    while start < initial_start_second_list:
        new_list.append(the_list[start])
        start += 1

    while list2_first_index <= end:
        new_list.append(the_list[list2_first_index])
        list2_first_index += 1
        
    for i in new_list:
        the_list[orig_start] = i
        orig_start += 1
        
    return the_list

def mergeSort(the_list):
    return _merge_sort((0, len(the_list) - 1), the_list)

print(daftar)
mergeSort(daftar)
print(daftar)
