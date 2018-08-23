/*
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
*/
class Solution {
public:
    string longestPalindrome(string s) {
        string r = "";
        int Cnt=0, i=0;
        bool ConFlag=true;
        int Head=0, Tail=0;
        
        if (s.length() < 2)
            return s;
        int n=s.length();
        while(n>1 && Head<=Tail) {
            i=Cnt;
            
            while(i>=0 && Head<=Tail) {
                r = s.substr(0+i, n);
                Head=0;
                Tail=r.length()-1;
                while((Head<=Tail) &&(r[Head] == r[Tail])) {Head++;Tail--;}
                i--;
            }
            
            Cnt++; n--;
        }
        if(Head<=Tail){
            return s.substr(s.length()-1, s.length());
        }
       
        return r;
    }
    
};

int main()
{
	string str;
	
	cout << "Please enter string: ";
	cin >> str;

    string res = Solution::longestPalindrome(str);
    cout << "Longest Palindromic Substring is \"" << res << "\""

    return(0);
}
