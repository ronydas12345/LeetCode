class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        step(0, 0, n, "", res);
        return res;
    }
                                                    //needs to be reference variable
    void step(int open, int closed, int n, string s, vector<string>& res) { // backtrack func
        if (open + closed == 2 * n) { // base case
            res.push_back(s);
            return;
        }

        if (open < n) { // add ( if possible
            step(open + 1, closed, n, s + "(", res);
        }

        if (closed < open) { // add ) only if possible
            step(open, closed + 1, n, s + ")", res);
        }
    }
};
