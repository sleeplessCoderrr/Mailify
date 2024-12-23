<script lang="ts">
    import type {Request} from "../../lib/interfaces/Request";

    export let activeTab: "send" | "reply";
    export let request:Request;
</script>

<div class="mt-6">
    <label class="block text-sm font-medium">Your Name</label>
    <input
            class="w-full mt-1 p-2 rounded border-2 border-stone-300 outline-none"
            type="text"
            placeholder="e.g., John Davis"
            bind:value={request.name}
    />

    <label class="block mt-4 text-sm font-medium">
        {activeTab === "send" ? "Receiver Name" : "Sender Name"}
    </label>
    <input
            class="w-full mt-1 p-2 rounded border-2 border-stone-300 outline-none"
            type="text"
            placeholder={activeTab === "send" ? "e.g., Elon Musk" : "e.g., John Doe"}
            bind:value={request.receiver}
    />

    <label class="block mt-4 text-sm font-medium">
        {activeTab === "send" ? "Receiver Email" : "Sender Email"}
    </label>
    <input
            class="w-full mt-1 p-2 rounded border-2 border-stone-300 outline-none"
            type="email"
            placeholder={activeTab === "send" ? "e.g., elon@mail.com" : "e.g., john@mail.com"}
            bind:value={request.receiverMail}
    />

    <label class="block mt-4 text-sm font-medium">
        {activeTab === "send" ? "What’s your email goal? Key points:" : "What’s your reply about? Key points:"}
    </label>
    <textarea
            class="w-full mt-1 p-2 rounded border-2 border-stone-300 outline-none h-32"
            placeholder={activeTab === "send" ? "Write your email goals here..." : "Write your reply key points here..."}
            bind:value={request.emailAbout}
    ></textarea>
</div>
