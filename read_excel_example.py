def read_excel(cfg):
    from common.data import ReadFromExcel
    read_data = ReadFromExcel()
    data_frame = read_data.from_xlsx(cfg)
    print(data_frame)


if __name__ == '__main__':
    cfg = {'io': 'data_manager/data/sample_data.xlsx'}
    read_excel(cfg)
