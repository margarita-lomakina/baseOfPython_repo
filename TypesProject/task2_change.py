m_list=input('Введите элементы списка через пробел: ').split()
print(m_list)

ind = 0
while ind + 1 < len(m_list):
    m_list[ind], m_list[ind+1] = m_list[ind+1], m_list[ind]
    ind += 2
print(m_list)