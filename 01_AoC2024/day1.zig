const std = @import("std");

pub fn main() !void {
    const max_bytes_per_line = 4096;
    var file = std.fs.cwd().openFile("test", .{}) catch {
        return;
    };
    defer file.close();

    var buffered_reader = std.io.bufferedReader(file.reader());
    const reader = buffered_reader.reader();

    const alloc = std.heap.page_allocator;

    var left = std.ArrayList(u8).init(alloc);
    var right = std.ArrayList(u8).init(alloc);
    defer left.deinit();
    defer right.deinit();

    while (try reader.readUntilDelimiterOrEofAlloc(alloc, '\n', max_bytes_per_line)) |line| {
        defer alloc.free(line);

        //const numbers = try std.fmt.parseInt(u32, line, 10);
        try left.append(line[0]);
        try right.append(line[1]);
    }

    std.debug.print("{s}\n", .{left.items});
    std.debug.print("{}\n", .{@TypeOf(left.items)});

    std.debug.print("{s}\n", .{right.items});
    std.debug.print("{}\n", .{@TypeOf(right.items)});
}
