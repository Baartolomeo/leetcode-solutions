//Time complexity: O(n)
//Space complexity: O(1)

/*Description.

Given an integer array data representing the data, return whether
it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data.
This means each integer represents only 1 byte of data.

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.

Example:
    Input: data = [197,130,1]
    Output: true
    Explanation: data represents the octet sequence: 11000101 10000010 00000001.
    It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

*/

class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int noBytesLeftInUTF = 0;
        for (int i = 0; i < data.size(); i++)
        {
            if (!noBytesLeftInUTF)
            {
                noBytesLeftInUTF = howManyBytesInChar(data[i]);
                if (!noBytesLeftInUTF)
                {
                    return false;
                }
            }
            else
            {
                if (!isCharByteValid(data[i]))
                {
                    return false;
                }
            }
            noBytesLeftInUTF--;
        }

        return noBytesLeftInUTF == 0;
    }

    int howManyBytesInChar(uint8_t data)
    {
        int noBytes = 0;
        if ((data >> 7) == 0)
        {
            noBytes = 1;
        }
        else if ((data >> 5) == 0b110)
        {
            noBytes = 2;
        }
        else if ((data >> 4) == 0b1110)
        {
            noBytes = 3;
        }else if ((data >> 3) == 0b11110)
        {
            noBytes = 4;
        }

        return noBytes;
    }

    bool isCharByteValid(uint8_t data)
    {
        return (data >> 6) == 0b10;
    }


};