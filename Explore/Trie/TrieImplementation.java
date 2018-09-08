import java.util.HashMap;

class Trie {    
  private class TrieNode {
    public Character value;
    public HashMap<Character, TrieNode> children;

    public TrieNode(Character ch) {
      value = ch;
      children = new HashMap<>();
    }
    
    public boolean hasChild(Character ch) {
      return children.get(ch) != null;
    }

    public void setChild(Character childValue) {
      if (hasChild(childValue)) return;
      children.put(childValue, new TrieNode(childValue));
    }
  }

  public TrieNode root;

  /** Initialize your data structure here. */
  public Trie() {
    root = new TrieNode(null);
  }
            
  /** Inserts a word into the trie. */
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
                
  /** Returns if the word is in the trie. */
  public boolean search(String word) {
    TrieNode cursor = root;
    for (int i = 0, len = word.length(); i < len; i++) {
      Character ch = new Character(word.charAt(i));
      if (!cursor.hasChild(ch)) return false;
      cursor = cursor.children.get(ch);
    }
    return cursor.hasChild(null);
  }
                    
  /** Returns if there is any word in the trie that starts
    * with the given prefix. */
  public boolean startsWith(String prefix) {
    TrieNode cursor = root;
    for (int i = 0, len = prefix.length(); i < len; i++) {
      Character ch = new Character(prefix.charAt(i));
      if (!cursor.hasChild(ch)) return false;
      cursor = cursor.children.get(ch);
    }
    return true;
  }
}

/** TODO: Code below for testing only. Delete upon submission. */
public class TrieImplementation {
  public static void main(String args[]) {
    Trie trie = new Trie();

    System.out.println("trie.insert(\"apple\")");
    trie.insert("apple");

    System.out.println("trie.search(\"apple\")");
    System.out.println("returns " + (trie.search("apple") ? "true" : "false"));
    
    System.out.println("trie.search(\"app\")");
    System.out.println("returns " + (trie.search("app") ? "true" : "false"));

    System.out.println("trie.startsWith(\"app\")");
    System.out.println("returns " + (trie.startsWith("app") ? "true" : "false"));

    System.out.println("trie.startsWith(\"apa\")");
    System.out.println("returns " + (trie.startsWith("apa") ? "true" : "false"));

    System.out.println("trie.insert(\"app\")");
    trie.insert("app");

    System.out.println("trie.search(\"app\")");
    System.out.println("returns " + (trie.search("app") ? "true" : "false"));
  }
}

