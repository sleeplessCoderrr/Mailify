<script>
    export let value = '';
    export let placeholder = "Recipient";
</script>

<div class="flex items-center space-x-2 mb-2">
    <span class="w-20 text-gray-600">To</span>
    <input
            type="email"
            bind:value
            placeholder={placeholder}
            class="flex-1 px-3 py-1.5 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
    />
</div>
