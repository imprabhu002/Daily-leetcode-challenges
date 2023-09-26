class Solution {
    public String removeDuplicateLetters(String s) {
        char[] charArray = s.toCharArray();
        int[] cnt = new int[26];
        int[] selected = new int[26];
        for (char c: charArray) cnt[c - 'a']++;
        int position = -1;
        for(char c: charArray) {
            if(selected[c-'a'] !=0){
                cnt[c-'a']--;
                continue;
            }
            while(position>=0 && charArray[position]>c && cnt[charArray[position] - 'a']>0) {
                selected[charArray[position]-'a']--;
                position--;
            }
            selected[c-'a']++;
            cnt[c-'a']--;
            charArray[++position] = c;
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<=position; i++){
            sb.append(charArray[i] + "");
        }
        return sb.toString();
    }
}
