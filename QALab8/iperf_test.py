import parser_iperf

class TestSuite:
    def test_iperf3_client_connection(self, client):
        output, error = client
        assert not error
        parse_result = parser_iperf.parser(output)

        # filter Transfer and Bitrate values
        for result in parse_result:
            transfer_value = float(result['Transfer'].split()[0])
            bitrate_value = float(result['Bitrate'].split()[0])
            min_transfer_value = 100
            min_bitrate_value = 1

            assert transfer_value >= min_transfer_value, f"Transfer value {transfer_value} is less than {min_transfer_value}"
            assert bitrate_value >= min_bitrate_value, f"Bitrate value {bitrate_value} is less than {min_bitrate_value}"
