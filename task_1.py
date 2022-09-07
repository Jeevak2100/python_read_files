import pandas as pd
import argparse
import os

"""""
Recursive Function To save the file
--input-file srcFile --output-dir output --max-bytes 500 --max-lines 100
"""""


def save_file_part(df, size_threshold,max_lines, save_path, part_number=0):
    file_size = df.memory_usage(index=False, deep=False).sum() / 4
    num_records = len(df)

    print('No of records in df {} '.format(num_records))
    print('file_size df {} '.format(file_size))
    print('max no of output lines {} '.format(max_lines))


    if file_size > size_threshold:
        records_to_split_off = int(num_records * size_threshold // file_size)

        print('No of records to fetch df {} '.format(records_to_split_off))
        if records_to_split_off > max_lines:
            records_to_split_off = max_lines

        df_to_save = df.head(records_to_split_off)
        file_size_df_to_save = df_to_save.memory_usage(index=False, deep=False).sum()
        print('file_size_df_to_save-df {} '.format(file_size_df_to_save))
        df_to_save.to_csv(save_path.format(part_number),sep=',', index=False, na_rep='NA',header=False)
        #  Recursive Call
        save_file_part(df.tail(num_records - records_to_split_off), size_threshold, max_lines, save_path,part_number= part_number + 1)

    else:
        df.to_csv(save_path.format(part_number), sep=',', index=False, na_rep='NA')


def print_hi(name):
    # 1. Program to Split a big file to small files
    """""
    Passing Arguments
    [a,b,c]
    5
    [1,2,3]
    """""
    print(f'Hi, {name}')
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--output-dir', type=str, required=True)
    parser.add_argument('--max-bytes', type=int, required=True)
    parser.add_argument('--max-lines', type=int, required=True)
    args = parser.parse_args()
    print(args.input_file)
    print(args.output_dir)
    print(args.max_bytes)
    print(args.max_lines)
    src_file_path = os.path.join(args.input_file, 'data.csv')
    print(src_file_path)
    out_file_path = os.path.join(args.output_dir, 'large-data-part{}.csv')
    print(out_file_path)

    # 2. Read source files
    df = pd.read_csv(src_file_path, sep=',')
    #    print(df)

    #
    save_file_part(df, args.max_bytes, args.max_lines, save_path=out_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('File-Splitter')

