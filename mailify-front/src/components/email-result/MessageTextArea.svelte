<script>
    export let value = '';
    export let placeholder = "Compose your email";
</script>

<textarea
        bind:value
        placeholder={placeholder}
        class="w-full h-40 px-3 py-1.5 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none"
></textarea>
