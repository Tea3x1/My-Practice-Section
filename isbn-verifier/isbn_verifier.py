def is_valid(isbn):

    isbn = isbn.replace("-", "")
    if len(isbn) == 10:
        if isbn.endswith("X") and isbn[0:9].isdigit() and "0" in isbn:
            return True

        else:
            result = []
            if isbn.isdigit():
                for number, ISBN in zip(isbn, range(10, 0, -1)):
                    result.append(int(number)*ISBN)

                result = sum(result) % 11

                return result == 0
            else:
                return False

    return False
