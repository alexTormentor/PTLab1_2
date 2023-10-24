import pytest
from ComplexLibrary import DataType, XMLDataReader

class TestXMLDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml_text = """<?xml version="1.0" encoding="UTF-8"?>
        <root>
            <student>
                <name>Иванов</name>
                <subject>
                    <name>математика</name>
                    <score>91</score>
                </subject>
                <subject>
                    <name>химия</name>
                    <score>100</score>
                </subject>
            </student>
            <student>
                <name>Петров</name>
                <subject>
                    <name>русский язык</name>
                    <score>87</score>
                </subject>
                <subject>
                    <name>литература</name>
                    <score>78</score>
                </subject>
            </student>
        </root>
        """
        data = {
            "Иванов": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return xml_text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
