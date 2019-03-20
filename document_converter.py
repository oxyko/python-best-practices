import tika


def convert_doc_to_txt():
    file_path = "test_data/test_ms_word.doc"
    output_path = "out_tmp/test_ms_word_doc.txt"

    from tika import parser
    parsed_obj = parser.from_file(file_path)

    with open(output_path, "w") as file_obj:
        file_obj.write(parsed_obj["content"])

if __name__ == "__main__":
    convert_doc_to_txt()