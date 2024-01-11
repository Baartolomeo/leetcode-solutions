// Time complexity: O(N)
// Space complexity: O(N)

/*
Given two strings first and second, consider occurrences in some text of the form "first second third", where second
comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

Example:
    Input:
        text = "alice is a good girl she is a good student",
        first = "a",
        second = "good"
    Output: ["girl","student"]
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** findOcurrences(char * text, char * first, char * second, int* returnSize){
*returnSize = 0;
    char *ptext = text, word[11];
    int char_in_word_counter = 0, words_counter = 0, occurrences_counter = 0;
    char **words      = malloc(100 * sizeof(char*)); //100 - max. number of words
    char **Occurrences = malloc(100 * sizeof(char*)); //100 - max. number of Occurences


    if (words == NULL || Occurrences == NULL)
        exit(EXIT_FAILURE);

    //Split text into words
    while (*ptext != '\0')
    {
        if (*ptext != ' ')
        {
            word[char_in_word_counter] = *ptext;
            char_in_word_counter++;
        }
        else
        {
            word[char_in_word_counter] = '\0';
            words[words_counter] = malloc(11 * sizeof(char));
            if (words[words_counter])
                strcpy(words[words_counter], word);
            else
                exit(EXIT_FAILURE);
            words_counter++;
            char_in_word_counter = 0;
        }
        ptext++;
    }

    word[char_in_word_counter] = '\0';
    words[words_counter] = malloc(11 * sizeof(char));
    if (words)
        strcpy(words[words_counter], word);
    else
        exit(EXIT_FAILURE);
    words_counter++;


    for (int i = 0; i < words_counter - 2; i++)
    {
        if (strcmp(words[i], first) == 0)
        {
            if (strcmp(words[i + 1], second) == 0)
            {
                Occurrences[occurrences_counter] = malloc(11 * sizeof(char));
                if (Occurrences)
                    strcpy(Occurrences[occurrences_counter], words[i + 2]);
                else
                    exit(EXIT_FAILURE);
                occurrences_counter++;
            }
        }
        free(words[i]);
    }
    free(words);

    Occurrences  = realloc (Occurrences, occurrences_counter * sizeof(char*));
    *returnSize = occurrences_counter;
    return Occurrences;
}