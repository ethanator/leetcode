import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class TrieNode {
  public Character value;
  public HashMap<Character, TrieNode> children = new HashMap<>();

  public TrieNode(Character ch) {
    value = ch;
  }

  public boolean hasChild(Character ch) {
    return children.get(ch) != null;
  }

  public void setChild(Character ch) {
    children.put(ch, new TrieNode(ch));
  }
}

class Trie {
  public static TrieNode root;

  public Trie() {
    root = new TrieNode(null);
  }

  public void insert(String word) {
    TrieNode cursor = root;
    for (int i = 0, len = word.length(); i < len; i++) {
      Character ch = new Character(word.charAt(i));
      if (!cursor.hasChild(ch)) {
        cursor.setChild(ch);
      }
      cursor = cursor.children.get(ch);
    }
    cursor.setChild(null);
  }

  public String match(String word) {
    TrieNode cursor = root;
    int i = 0;
    boolean matched = false;
    for (int len = word.length(); i < len; i++) {
      Character ch = new Character(word.charAt(i));
      if (cursor.hasChild(null)) {
        matched = true;
        break;
      }
      if (!cursor.hasChild(ch)) {
        break;
      }
      cursor = cursor.children.get(ch);
    }
    return matched ? word.substring(0, i) : word;
  }
}

class Solution {
  public String replaceWords(List<String> dict, String sentence) {
    Trie trie = new Trie();
    for (String root : dict) {
      trie.insert(root);
    }
    List<String> words = Arrays.asList(sentence.split(" "));
    List<String> replacedWords = new ArrayList<>();
    for (int i = 0, len = words.size(); i < len; i++) {
      String word = words.get(i);
      replacedWords.add(trie.match(word));
    }
    return String.join(" ", replacedWords);
  }
}

public class ReplaceWords {
  public static void main(String[] args) {
    // Input: dict = ["cat", "bat", "rat"]
    // sentence = "the cattle was rattled by the battery"
    // Output: "the cat was rat by the bat"
    List<String> dict = new ArrayList<>();
    dict.add("cat");
    dict.add("bat");
    dict.add("rat");
    String sentence = "the cattle was rattled by the battery";
    Solution solution = new Solution();
    System.out.println(solution.replaceWords(dict, sentence));
  }
}