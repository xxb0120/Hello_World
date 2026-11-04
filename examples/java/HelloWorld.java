/**
 * A tiny command-line "Hello, World!" program.
 *
 * <p>Run it with no arguments to greet the world:
 *
 * <pre>{@code java HelloWorld.java}</pre>
 *
 * <p>Pass a name to greet someone specific:
 *
 * <pre>{@code java HelloWorld.java Alice}</pre>
 */
public class HelloWorld {

    public static void main(String[] args) {
        String name = args.length > 0 ? args[0].strip() : "World";
        if (name.isEmpty()) {
            System.err.println("error: name must not be empty");
            System.exit(2);
        }
        System.out.println("Hello, " + name + "!");
    }
}
