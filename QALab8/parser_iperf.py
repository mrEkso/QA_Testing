import re

def parser(output):
    parser_results = []
    lines = output.splitlines()
    for line in lines:
        is_match = re.search(r'([\d.]+-\s+[\d.]+)\s+sec\s+([\d.]+\s+\w?Bytes)\s+([\d.]+\s+\w?bits/sec)\s+([\d.]+)\s+([\d.]+\s+\w?Bytes)', line)
        if is_match:
            check_match = {
                'Interval': is_match.group(1),
                'Transfer': is_match.group(2),
                'Bitrate': is_match.group(3),
                'Retr': is_match.group(4),
                'Cwnd': is_match.group(5)
            }
            parser_results.append(check_match)
    return parser_results
