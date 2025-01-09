#include <iostream>
#include <vector>

class Solution
{
public:
//TIME LIMIT EXCCEDED, BUT GOOD THING IT WORKS
    std::vector<int> dailyTemperatures(std::vector<int> &temperatures)
    {

        std::vector<int> res;
        for (int i = 0; i < temperatures.size(); i++)
        {
            int days_diff = 0;
            for (int j = i + 1; j < temperatures.size(); j++)
            {
                int diff = temperatures[j] - temperatures[i];
                if (diff > 0)
                {
                    days_diff = j - i;
                    break;
                }

            }
            res.push_back(days_diff);
        }
        return res;
    }
    std::vector<int> = 
};
int main()
{
    std::vector<int> temperature = {73, 74, 75, 71, 69, 72, 76, 73};
    Solution obj;
    std::vector<int> result = obj.dailyTemperatures(temperature);
    for (int days : result)
    {
        std::cout << "days to wait: " << days << std::endl;
    }
    return 0;
}