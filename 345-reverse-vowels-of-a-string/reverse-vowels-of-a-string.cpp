
class Solution {
public:
    string reverseVowels(string s) {
        int n = s.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            
            bool is_vowel_i = (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' ||
                               s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U');
            
           
            bool is_vowel_j = (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u' ||
                               s[j] == 'A' || s[j] == 'E' || s[j] == 'I' || s[j] == 'O' || s[j] == 'U');
            
            if (is_vowel_i && is_vowel_j) {
                swap(s[i], s[j]);
                i++;
                j--;
            } else if (is_vowel_i) {
                j--;
            } else {
                i++;
            }
        }
        return s;
    }
};
